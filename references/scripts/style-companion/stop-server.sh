#!/usr/bin/env bash
# Stop a Visual HTML style gallery server session.

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: stop-server.sh <session-dir>" >&2
  exit 2
fi

SESSION_DIR="$(cd "$1" && pwd)"
PID_FILE="$SESSION_DIR/state/server.pid"
if [[ ! -f "$PID_FILE" ]]; then
  echo "No running gallery server found in $SESSION_DIR" >&2
  exit 1
fi

PID="$(cat "$PID_FILE")"
if kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  for _ in {1..50}; do
    kill -0 "$PID" 2>/dev/null || break
    sleep 0.1
  done
fi
rm -f "$PID_FILE"
