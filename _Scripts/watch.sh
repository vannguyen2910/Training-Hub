#!/bin/bash
# watch.sh — watches a lesson's markdown and syncs to HTML on save.
#
# Usage:
#   ./watch.sh <lesson-folder>              watch one lesson
#   ./watch.sh                              watch ALL lessons under Library/
#
# First-time setup:
#   brew install fswatch
#   pip3 install markdown

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$REPO_ROOT/_Scripts/sync-lesson.py"

if ! command -v fswatch &>/dev/null; then
  echo "fswatch not found. Run: brew install fswatch"
  exit 1
fi

if [ -n "$1" ]; then
  # Single lesson mode
  LESSON_DIR="$REPO_ROOT/$1"
  WATCH_PATH="$LESSON_DIR/learning"
  echo "👁  Watching: $1/learning/"
  echo "    Press Ctrl+C to stop."
  fswatch --latency 2 -o "$WATCH_PATH" | while read; do
    echo "Change detected — syncing $1…"
    python3 "$SCRIPT" "$LESSON_DIR"
  done
else
  # All lessons mode
  WATCH_PATH="$REPO_ROOT/Library"
  echo "👁  Watching all lessons under Library/"
  echo "    Press Ctrl+C to stop."
  fswatch --latency 2 -o "$WATCH_PATH" --include=".*\.md$" --exclude=".*" | while read changed; do
    # Find the lesson folder (3 levels up from the .md file)
    LESSON=$(echo "$changed" | grep -o ".*/Library/[^/]*/[^/]*/[^/]*" | head -1)
    if [ -n "$LESSON" ]; then
      echo "Change detected — syncing $(basename "$LESSON")…"
      python3 "$SCRIPT" "$LESSON"
    fi
  done
fi
