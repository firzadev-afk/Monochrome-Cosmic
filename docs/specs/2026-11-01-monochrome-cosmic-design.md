# Design: Monochrome-Cosmic (2026-11-01)

Status: approved by operator ("lakukan"), built same day.

## Intent

Who: firzadev-afk, COSMIC desktop user, now maintainer.
Why now: the operator wants one owned, self-maintained project that
takes its artwork directly from the original YAMIS repository on
Bitbucket and integrates it properly with COSMIC, instead of
depending on an unmaintained copy.
Success: every installed application shows a monochrome glyph that is
recognizably its real logo; repository and local install never drift.

## Decisions (operator)

- Name: **Monochrome-Cosmic** (own brand; Dirn/YAMIS credited, GPL kept).
- Scope: import ALL upstream YAMIS icons (Bitbucket v1.6.2), slim the
  duplicates instead of starting small.
- "Duplicate" means: one real file per logo; other names are symlinks;
  unused exact copies and case-only duplicates collapse into aliases.
- A dedicated agent skill is mandatory for icon creation: source the
  real logo first, monochrome it, redraw by hand in SVG when needed,
  matching the original likeness totally; always improve, never settle
  for a generic placeholder. Skill ships in this repo under `skills/`
  and in the operator's myskills.

## Decisions (builder)

- Repo layout: `theme/` (installable theme), `docs/`, `scripts/`,
  `skills/`. The installed theme is a symlink
  `~/.local/share/icons/Monochrome-Cosmic -> <repo>/theme`, so local
  and project are literally the same files.
- Upstream variant `mimetypes/scalable-outlined` (746 files) is not
  imported; the filled mimetype set is the single style.
- SVG internals of upstream artwork are not rewritten; the drawing
  standards govern new icons.

## Build checklist

- [x] Clone upstream YAMIS v1.6.2
- [x] Import with dedupe (2,616 real files, 2,939 symlinks)
- [x] Overlay custom icons from the previous project
- [x] Clean `index.theme` for Monochrome-Cosmic
- [x] README, STANDARDS, LICENSE, credits
- [x] install.sh (symlink install + icon cache)
- [x] Skill `monochrome-icon-forge` + evals (repo + myskills)
- [x] GitHub repo created, first commit pushed
- [x] Theme installed and lookups verified
- [x] Panel processes restarted; old theme fully replaced by Monochrome-Cosmic

## Non-goals

- Editing any application's own icon or `.desktop` files.
- Repainting upstream artwork wholesale.
- Supporting non-COSMIC desktops beyond what freedesktop gives free.
