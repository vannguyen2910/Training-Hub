#!/usr/bin/env python3
"""
watcher.py — Knowledge Library Folder Watcher
Winnie Nguyen · UX Mentoring Hub

Polls lessons/, frameworks/, guides/, slides/ every 3 seconds.
When a new subfolder appears, automatically runs build.py.

Started automatically by start-library.command.
You do not need to run this manually.
"""

import os
import sys
import time
import subprocess
from pathlib import Path

SCRIPT_DIR  = Path(__file__).parent
POLL_SECS   = 3
TYPE_DIRS   = ["lessons", "frameworks", "guides", "slides"]

CYAN   = "\033[36m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


def get_subfolders():
    """Return a set of (type_dir, folder_name) pairs that currently exist."""
    found = set()
    for type_dir in TYPE_DIRS:
        path = SCRIPT_DIR / type_dir
        if path.is_dir():
            for entry in path.iterdir():
                if entry.is_dir():
                    found.add((type_dir, entry.name))
    return found


def run_build():
    print(f"\n{BOLD}{CYAN}  ▶  New folder detected — running build.py…{RESET}")
    result = subprocess.run(
        [sys.executable, str(SCRIPT_DIR / "build.py")],
        cwd=str(SCRIPT_DIR),
        capture_output=True,
        text=True,
    )
    # Print build output with indent
    for line in result.stdout.splitlines():
        print(f"     {line}")
    if result.returncode == 0:
        print(f"{GREEN}  ✓  Build complete.{RESET}\n")
    else:
        print(f"{YELLOW}  ⚠  Build finished with warnings:{RESET}")
        for line in result.stderr.splitlines():
            print(f"     {line}")
        print()


def main():
    print(f"\n{BOLD}  👁  Library Watcher started{RESET}")
    print(f"  Watching: {', '.join(TYPE_DIRS)}")
    print(f"  Drop a new folder in any of these → build runs automatically.")
    print(f"  (Checking every {POLL_SECS}s — Ctrl+C to stop)\n")

    known = get_subfolders()

    while True:
        time.sleep(POLL_SECS)
        try:
            current = get_subfolders()
            new = current - known
            if new:
                for type_dir, name in sorted(new):
                    print(f"  ✦  New folder: {type_dir}/{name}/")
                known = current
                run_build()
                known = get_subfolders()   # refresh after build (build may create subfolders)
        except KeyboardInterrupt:
            print(f"\n  Watcher stopped.\n")
            sys.exit(0)
        except Exception as e:
            print(f"  ⚠  Watcher error: {e}")


if __name__ == "__main__":
    main()
