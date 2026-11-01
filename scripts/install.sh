#!/usr/bin/env bash
# Install Monochrome-Cosmic as a symlink so the installed theme and
# this repository are always the same files.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$HOME/.local/share/icons/Monochrome-Cosmic"

mkdir -p "$HOME/.local/share/icons"
if [ -L "$TARGET" ] || [ ! -e "$TARGET" ]; then
  ln -sfn "$REPO_DIR/theme" "$TARGET"
else
  echo "ERROR: $TARGET exists and is not a symlink; move it away first." >&2
  exit 1
fi

gtk-update-icon-cache -f "$TARGET" || true
echo "Installed: $TARGET -> $REPO_DIR/theme"
echo "Select 'Monochrome-Cosmic' in COSMIC Settings > Desktop > Appearance."
