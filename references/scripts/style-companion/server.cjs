#!/usr/bin/env node

const fs = require('fs');
const http = require('http');
const path = require('path');
const crypto = require('crypto');

const SESSION_DIR = path.resolve(process.env.VISUAL_HTML_SESSION_DIR || '.visual-html-companion');
const STATE_DIR = path.join(SESSION_DIR, 'state');
const GALLERY_FILE = path.resolve(process.env.VISUAL_HTML_GALLERY || path.join(__dirname, '../../style-gallery.html'));
const ASSET_ROOT = path.dirname(GALLERY_FILE);
const HOST = process.env.VISUAL_HTML_HOST || '127.0.0.1';
const REQUESTED_PORT = Number(process.env.VISUAL_HTML_PORT || 0);
const TOKEN = process.env.VISUAL_HTML_TOKEN || crypto.randomBytes(24).toString('hex');
const MAX_BODY_BYTES = 64 * 1024;
const EVENTS_FILE = path.join(STATE_DIR, 'events');
const INFO_FILE = path.join(STATE_DIR, 'server-info');
const PID_FILE = path.join(STATE_DIR, 'server.pid');
const COOKIE_NAME = 'visual-html-session';

fs.mkdirSync(STATE_DIR, { recursive: true, mode: 0o700 });

function safeEqual(left, right) {
  const a = Buffer.from(String(left || ''));
  const b = Buffer.from(String(right || ''));
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

function queryKey(url) {
  try { return new URL(url, 'http://localhost').searchParams.get('key'); } catch { return null; }
}

function cookieKey(request) {
  const cookies = String(request.headers.cookie || '').split(';');
  const entry = cookies.find(item => item.trim().startsWith(`${COOKIE_NAME}=`));
  return entry ? entry.trim().slice(COOKIE_NAME.length + 1) : null;
}

function isAuthorized(request) {
  return safeEqual(queryKey(request.url), TOKEN) || safeEqual(cookieKey(request), TOKEN);
}

function setSessionCookie(response) {
  response.setHeader('Set-Cookie', `${COOKIE_NAME}=${TOKEN}; HttpOnly; SameSite=Strict; Path=/`);
}

function send(response, status, body, contentType = 'text/plain; charset=utf-8') {
  response.writeHead(status, { 'content-type': contentType, 'cache-control': 'no-store' });
  response.end(body);
}

function json(response, status, body) {
  send(response, status, JSON.stringify(body), 'application/json; charset=utf-8');
}

function companionBootstrap() {
  return `<script>(function () {
    const endpoint = '/__visual_html/events';
    window.visualHtmlCompanion = Object.freeze({
      send: async function (event) {
        const response = await fetch(endpoint, {
          method: 'POST',
          credentials: 'same-origin',
          headers: { 'content-type': 'application/json' },
          body: JSON.stringify(event)
        });
        if (!response.ok) throw new Error('选择事件提交失败（HTTP ' + response.status + '）');
        return response.json();
      }
    });
  }());</script>`;
}

function galleryHtml() {
  const source = fs.readFileSync(GALLERY_FILE, 'utf8');
  const marker = '</head>';
  if (!source.includes(marker)) throw new Error(`Gallery is missing ${marker}: ${GALLERY_FILE}`);
  return source.replace(marker, `${companionBootstrap()}${marker}`);
}

function safeAssetPath(urlPath) {
  const decoded = decodeURIComponent(urlPath.split('?')[0]);
  if (!decoded.startsWith('/styles/')) return null;
  const candidate = path.resolve(ASSET_ROOT, `.${decoded}`);
  return candidate.startsWith(`${ASSET_ROOT}${path.sep}`) ? candidate : null;
}

function readBody(request) {
  return new Promise((resolve, reject) => {
    let total = 0;
    const chunks = [];
    request.on('data', chunk => {
      total += chunk.length;
      if (total > MAX_BODY_BYTES) {
        reject(new Error('request body too large'));
        request.destroy();
        return;
      }
      chunks.push(chunk);
    });
    request.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    request.on('error', reject);
  });
}

function validateEvent(value) {
  if (!value || value.type !== 'style-selected') throw new Error('unsupported event type');
  for (const field of ['styleId', 'styleName', 'prompt']) {
    if (typeof value[field] !== 'string' || value[field].length === 0 || value[field].length > 1000) {
      throw new Error(`invalid ${field}`);
    }
  }
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(value.styleId)) throw new Error('invalid styleId');
  return {
    type: value.type,
    choice: value.styleId,
    styleId: value.styleId,
    styleName: value.styleName,
    prompt: value.prompt,
    text: value.prompt,
    timestamp: Date.now()
  };
}

async function handle(request, response) {
  if (!isAuthorized(request)) {
    send(response, 403, 'Session key required. Open the complete URL returned by start-server.sh.');
    return;
  }
  setSessionCookie(response);

  const requestUrl = new URL(request.url, `http://${HOST}`);
  if (request.method === 'GET' && (requestUrl.pathname === '/' || requestUrl.pathname === '/index.html')) {
    try { send(response, 200, galleryHtml(), 'text/html; charset=utf-8'); }
    catch (error) { send(response, 500, error.message); }
    return;
  }

  if (request.method === 'GET' && requestUrl.pathname === '/__visual_html/status') {
    json(response, 200, { ok: true, sessionDir: SESSION_DIR });
    return;
  }

  if (request.method === 'POST' && requestUrl.pathname === '/__visual_html/events') {
    try {
      const event = validateEvent(JSON.parse(await readBody(request)));
      fs.appendFileSync(EVENTS_FILE, `${JSON.stringify(event)}\n`, { mode: 0o600 });
      json(response, 200, { ok: true, choice: event.choice });
    } catch (error) {
      json(response, 400, { ok: false, error: error.message });
    }
    return;
  }

  if (request.method === 'GET') {
    const assetPath = safeAssetPath(requestUrl.pathname);
    if (assetPath && fs.existsSync(assetPath) && fs.statSync(assetPath).isFile()) {
      const extension = path.extname(assetPath).toLowerCase();
      const contentTypes = {
        '.html': 'text/html; charset=utf-8',
        '.png': 'image/png',
        '.svg': 'image/svg+xml',
        '.css': 'text/css; charset=utf-8',
        '.js': 'text/javascript; charset=utf-8'
      };
      send(response, 200, fs.readFileSync(assetPath), contentTypes[extension] || 'application/octet-stream');
      return;
    }
  }

  send(response, 404, 'Not found');
}

const server = http.createServer((request, response) => {
  handle(request, response).catch(error => {
    if (!response.headersSent) send(response, 500, error.message);
    else response.destroy();
  });
});

server.on('error', error => {
  console.error(JSON.stringify({ type: 'server-error', error: error.message }));
  process.exitCode = 1;
});

server.listen(REQUESTED_PORT, HOST, () => {
  const address = server.address();
  const port = typeof address === 'object' ? address.port : REQUESTED_PORT;
  fs.writeFileSync(PID_FILE, `${process.pid}\n`, { mode: 0o600 });
  const info = {
    type: 'server-started',
    port,
    host: HOST,
    url: `http://${HOST}:${port}/?key=${encodeURIComponent(TOKEN)}`,
    session_dir: SESSION_DIR,
    state_dir: STATE_DIR,
    gallery: GALLERY_FILE
  };
  fs.writeFileSync(INFO_FILE, `${JSON.stringify(info)}\n`, { mode: 0o600 });
  console.log(JSON.stringify(info));
});

function stop(reason) {
  fs.writeFileSync(path.join(STATE_DIR, 'server-stopped'), `${JSON.stringify({ reason, timestamp: Date.now() })}\n`, { mode: 0o600 });
  fs.rmSync(PID_FILE, { force: true });
  server.close(() => process.exit(0));
}

process.on('SIGTERM', () => stop('sigterm'));
process.on('SIGINT', () => stop('sigint'));
