#!/bin/bash
# ─────────────────────────────────────────────────────────
#  Knowledge Library — Local Server + Auto-Builder
#  Double-click this file to start everything.
#  Press Ctrl+C in this window to stop.
# ─────────────────────────────────────────────────────────

cd "$(dirname "$0")"

# Check Python is available
if ! command -v python3 &> /dev/null; then
  echo "⚠️  Python 3 is not installed."
  echo "Install it from https://www.python.org or via Homebrew: brew install python3"
  read -p "Press Enter to close..."
  exit 1
fi

# Pick a port (default 8000, fallback 8001 if taken)
PORT=8000
if lsof -i :$PORT &> /dev/null; then
  PORT=8001
fi

echo ""
echo "  ┌────────────────────────────────────────────┐"
echo "  │   Winnie Nguyen — Knowledge Library        │"
echo "  │                                            │"
echo "  │   Server  →  http://localhost:$PORT           │"
echo "  │   Watcher →  watching for new folders      │"
echo "  │                                            │"
echo "  │   Press Ctrl+C to stop everything          │"
echo "  └────────────────────────────────────────────┘"
echo ""

# ── Run build once on startup to catch any changes made while offline ───
echo "  Running build…"
python3 build.py
echo ""

# ── Start folder watcher in the background ──────────────────────────────
python3 watcher.py &
WATCHER_PID=$!

# ── Open browser (slight delay so server starts first) ──────────────────
sleep 0.6 && open "http://localhost:$PORT" &

# ── Start HTTP server (foreground — Ctrl+C stops everything) ────────────
trap "kill $WATCHER_PID 2>/dev/null; echo '  Stopped.'" EXIT
python3 -m http.server $PORT
