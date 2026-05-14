#!/bin/bash
# new-lesson.sh — scaffold a new lesson, framework, guide, or slides folder.
#
# Usage:
#   ./new-lesson.sh lesson   <folder-name>
#   ./new-lesson.sh framework <folder-name>
#   ./new-lesson.sh guide    <folder-name>
#   ./new-lesson.sh slides   <folder-name>
#
# Example:
#   ./new-lesson.sh lesson user-journey-mapping

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$REPO_ROOT/Library/build.py"

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: ./new-lesson.sh <type> <folder-name>"
  echo "Types: lesson | framework | guide | slides"
  exit 1
fi

python3 "$BUILD" --new "$1" "$2"
