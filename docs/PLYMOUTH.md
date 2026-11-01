# Monochrome boot splash (Plymouth)

The desktop icons are only half of boot-to-desktop consistency: the
Plymouth splash can match too.

`scripts/make-plymouth-theme.sh` builds **Monochrome Dreamboat**
from the installed CachyOS `dreamboat` theme: every image
(animation frames, throbber, password dialog artwork, and the
"Hello, Dreamboat!" watermark) is converted to grayscale, so the
whole boot sequence renders in black, white, and gray. The script
installs it as the default Plymouth theme and rebuilds the
initramfs (`mkinitcpio -P`, Limine-aware on CachyOS).

Run it with:

```bash
bash scripts/make-plymouth-theme.sh
```

Revert at any time:

```bash
sudo plymouth-set-default-theme dreamboat
sudo mkinitcpio -P
```

The splash only covers the OS boot stage. The firmware vendor logo
shown by UEFI before Plymouth starts comes from the machine's ACPI
BGRT table and cannot be changed from the operating system.
