#!/usr/bin/env bash
# Build and install the Monochrome-Cosmic Plymouth boot theme.
#
# Takes the installed "dreamboat" theme (CachyOS), converts every
# image to grayscale so the boot animation, throbber, and the
# "Hello, Dreamboat!" watermark render in black/white/gray only,
# installs it as "monochrome-dreamboat", and rebuilds the initramfs.
#
# Revert: sudo plymouth-set-default-theme dreamboat && sudo mkinitcpio -P
set -euo pipefail

SRC=/usr/share/plymouth/themes/dreamboat
NAME=monochrome-dreamboat
DST=/usr/share/plymouth/themes/$NAME
BUILD=$(mktemp -d)

[ -d "$SRC" ] || { echo "dreamboat theme not found at $SRC" >&2; exit 1; }

cp -r "$SRC/." "$BUILD/"
rm -f "$BUILD/dreamboat.plymouth"

# Convert all artwork to grayscale (alpha preserved).
find "$BUILD" -name '*.png' -print0 | while IFS= read -r -d '' png; do
  magick "$png" -colorspace Gray "$png"
done

# Theme descriptor, pointing at the new directory.
sed -e "s/^Name=.*/Name=Monochrome Dreamboat/" \
    -e "s|^ImageDir=.*|ImageDir=$DST|" \
    "$SRC/dreamboat.plymouth" > "$BUILD/$NAME.plymouth"

sudo install -d "$DST"
sudo cp -r "$BUILD/." "$DST/"
rm -rf "$BUILD"

sudo plymouth-set-default-theme "$NAME"
echo "Default theme: $(plymouth-set-default-theme)"

sudo mkinitcpio -P
echo "Done. Reboot to see the monochrome boot animation."
