# Monochrome-Cosmic

Monochrome icon set for the COSMIC Desktop Environment. Every app icon is a
single-color glyph (`#d8dee9` via `currentColor`) on a transparent
background, so the whole desktop reads as one consistent set.

Maintained by [firzadev-afk](https://github.com/firzadev-afk).

## Origin and license

The icon artwork originates from YAMIS (Yet Another Monochrome Icon Set)
by Dirn — <https://bitbucket.org/dirn-typo/yet-another-monochrome-icon-set> —
via the COSMIC fork by harpoonwithaz. This repository is an independent,
reorganized continuation: folder layout, file naming, and icon creation
follow the project standards in [docs/STANDARDS.md](docs/STANDARDS.md).

Licensed under the GNU General Public License, consistent with the
original source. See [LICENSE](LICENSE).

## Install

```bash
git clone https://github.com/firzadev-afk/Monochrome-Cosmic.git
cd Monochrome-Cosmic
bash scripts/install.sh
```

Then select **Monochrome-Cosmic** in COSMIC Settings > Desktop >
Appearance > Icons and toolkit theming. Log out and back in once if
icons do not refresh.

## Layout

```text
theme/     the installable icon theme (index.theme + context folders)
docs/      standards and design documents
scripts/   install and upstream-sync tooling
skills/    agent skill for creating new monochrome icons
```

One real file per logo; every other name an application uses for the
same logo is a symlink to that file. See
[docs/STANDARDS.md](docs/STANDARDS.md) for the full rules.
