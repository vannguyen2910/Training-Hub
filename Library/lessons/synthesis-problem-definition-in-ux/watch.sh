#!/bin/bash
# watch.sh — watches Synthesis & Problem Definition.md and syncs to HTML on save
#
# First-time setup:
#   brew install fswatch
#   pip3 install markdown

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MARKDOWN="$SCRIPT_DIR/learning/Synthesis & Problem Definition.md"

if ! command -v fswatch &>/dev/null; then
  echo "fswatch not found. Run: brew install fswatch"
  exit 1
fi

echo "👁  Watching: Synthesis & Problem Definition.md"
echo "    Changes will sync to synthesis-problem-definition-in-ux.html automatically."
echo "    Press Ctrl+C to stop."
echo ""

# --latency 2: debounce — waits 2s after last save before firing
fswatch --latency 2 -o "$MARKDOWN" | while read; do
  echo "Change detected — syncing..."
  python3 "$SCRIPT_DIR/sync-lesson.py"
done
