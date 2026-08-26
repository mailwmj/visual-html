#!/usr/bin/env bash
# Start the Visual HTML style-selection companion and print connection info.
# Usage: start-server.sh [--project-dir <path>] [--open] [--foreground]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
PROJECT_DIR=""
OPEN_BROWSER="false"
FOREGROUND="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project-dir)
      PROJECT_DIR="$2"
      shift 2
      ;;
    --open)
      OPEN_BROWSER="true"
      shift
      ;;
    --foreground)
      FOREGROUND="true"
      shift
      ;;
    *)
      echo "{\"error\":\"Unknown argument: $1\"}" >&2
      exit 2
      ;;
  esac
done

if [[ -z "$PROJECT_DIR" ]]; then
  PROJECT_DIR="$REPO_ROOT"
fi
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"

# Codex reaps detached processes when the launching shell exits. Keep the
# server attached in that harness so it remains available for the next turn.
if [[ -n "${CODEX_CI:-}" ]]; then
  FOREGROUND="true"
fi

SESSION_ID="$(date +%s)-$$"
SESSION_DIR="$PROJECT_DIR/.visual-html/companion/$SESSION_ID"
STATE_DIR="$SESSION_DIR/state"
mkdir -p "$STATE_DIR"
chmod 700 "$SESSION_DIR" "$STATE_DIR"

TOKEN="$(node -e "process.stdout.write(require('crypto').randomBytes(24).toString('hex'))")"
export VISUAL_HTML_SESSION_DIR="$SESSION_DIR"
export VISUAL_HTML_GALLERY="$REPO_ROOT/references/style-gallery.html"
export VISUAL_HTML_TOKEN="$TOKEN"

if [[ "$FOREGROUND" == "true" ]]; then
  node "$SCRIPT_DIR/server.cjs"
  exit $?
fi

LOG_FILE="$STATE_DIR/server.log"
nohup node "$SCRIPT_DIR/server.cjs" > "$LOG_FILE" 2>&1 &
SERVER_PID=$!
echo "$SERVER_PID" > "$STATE_DIR/server.pid"

for _ in {1..50}; do
  if [[ -f "$STATE_DIR/server-info" ]]; then
    INFO="$(cat "$STATE_DIR/server-info")"
    # Codex can open the returned URL in its in-app Browser. Do not launch a
    # separate OS browser from that harness; outside Codex, --open remains a
    # convenient fallback for the user's default browser.
    if [[ "$OPEN_BROWSER" == "true" && -z "${CODEX_CI:-}" ]]; then
      URL="$(node -e 'const fs=require("fs"); const info=JSON.parse(fs.readFileSync(process.argv[1],"utf8")); process.stdout.write(info.url)' "$STATE_DIR/server-info")"
      if command -v open >/dev/null 2>&1; then
        open "$URL" >/dev/null 2>&1 || true
      elif command -v xdg-open >/dev/null 2>&1; then
        xdg-open "$URL" >/dev/null 2>&1 || true
      fi
    fi
    printf '%s\n' "$INFO"
    exit 0
  fi
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then
    cat "$LOG_FILE" >&2 || true
    exit 1
  fi
  sleep 0.1
done

cat "$LOG_FILE" >&2 || true
echo '{"error":"Server failed to start within 5 seconds"}' >&2
exit 1
