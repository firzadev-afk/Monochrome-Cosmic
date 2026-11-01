---
name: monochrome-icon-forge
description: Use when an application icon must be created, converted, or fixed as a single-color monochrome glyph for the Monochrome-Cosmic icon theme, when an app still shows a colorful or generic placeholder icon, or when a logo from the internet or an AI image model must become a clean SVG icon that matches the original logo exactly.
license: GPL-3.0
compatibility: opencode
metadata:
  version: "1.0.0"
  reviewed: "2026-11"
  category: "06-frontend"
---
# Monochrome Icon Forge

# Overview

Create monochrome app icons that are recognizably the application's
real logo, drawn as one clean SVG glyph in the Monochrome-Cosmic
style. The original logo is the source of truth: find it first,
convert or redraw it faithfully, and improve it until it survives
small sizes. Never invent a generic substitute.

Born from a recorded failure: without this skill, an agent asked for
a Freebuff icon invented a single letter "F" with a fake terminal
cursor, put it on a dark rounded square, used a 48x48 canvas and a
literal gray fill, and suggested editing the app's own files. Every
rule below closes one of those failures.

## When to Use

- An installed app still shows its colorful original icon, a generic
  placeholder, or another app's glyph in COSMIC.
- A new application needs an icon in the Monochrome-Cosmic theme.
- A logo found online (brand page, Simple Icons, app website) must
  become a monochrome SVG.
- An AI-generated or PNG-traced logo must be cleaned into a proper
  glyph.
- An existing icon in the set looks wrong, blurry, or off-style.

## When NOT to Use

- Changing wallpapers, accent colors, or `.ron` color themes; this
  skill is only for application icon glyphs.
- Editing an application's own files, `.desktop` entries, or the
  system `hicolor` theme to force an icon. All customization lives
  inside the Monochrome-Cosmic theme folder.
- Creating colorful, multi-brand, or photographic icons.

## Workflow

1. Find the exact icon name. Read the app's `.desktop` file and take
   its `Icon=` value verbatim (case-sensitive). That value, plus
   `.svg`, is the file name. Verify: the name matches a real desktop
   entry, not a guess from the app's display name.
2. Source the original logo, in this order: (a) icon already in
   upstream YAMIS or this theme under another name, (b) the app's
   installed original icon (`hicolor` PNG/SVG or `/usr/share/pixmaps`),
   (c) Simple Icons or the vendor brand page, (d) the app's website
   or repository assets. Verify: you can display the original logo
   image before drawing anything.
3. Choose the conversion path. Existing SVG: strip every color to a
   single fill. PNG/JPG with a simple geometric logo: redraw it by
   hand as SVG paths over the original. Complex or photographic
   logo: simplify to its signature silhouette; if no silhouette
   survives 24 px, use the closest existing monochrome glyph in the
   theme and say so. Verify: the path taken is named in your report.
4. Draw to the house standard: `viewBox="0 0 16.933 16.933"`,
   transparent background, no background plate or rounded square,
   every path `class="ColorScheme-Text"` with
   `style="fill:currentColor"`, and
   `.ColorScheme-Text {color:#d8dee9}` in a `<style>` def. Verify:
   the file contains no other fill color and no `<rect>` backdrop.
5. Check total likeness. Render the new icon and the original logo
   side by side at 16, 24, and 48 px on a dark background. Silhouette,
   proportions, and signature details must match; details that vanish
   at 24 px are simplified, never replaced with invented details.
   Verify: at 24 px a viewer names the same app from both images.
6. Improve, do not settle. If the glyph reads poorly at small size,
   thicken strokes, close hairline gaps, and remove inner detail
   before adding the file. A generic placeholder (gear, folder,
   letter) is a failed result, not a fallback. Verify: at least one
   improvement pass happened whenever the first render was unclear.
7. Place and alias. Save the real file in
   `theme/apps/scalable/` (or the matching context folder) of the
   Monochrome-Cosmic repository. Every other name apps use for the
   same logo becomes a symlink to it; never copy the file and never
   touch files outside the repository. Verify: the file resolves
   through the theme's `index.theme` contexts.
8. Refresh and prove. Run `gtk-update-icon-cache` on the installed
   theme, restart `cosmic-panel`, `cosmic-launcher`, and
   `cosmic-app-library` (they cache icons in memory), then verify a
   GTK icon lookup for the exact `Icon=` name returns the new file.
   Verify: lookup output path is inside Monochrome-Cosmic.
9. Sync. Commit with a message naming the icon and its source, and
   push. Pull first if GitHub moved. Verify: `git status` is clean
   and local equals `origin/main`.

## Output Contract

For each icon, deliver:

- The SVG file at its theme path, following step 4 exactly.
- Symlinks for alias names, when the app is known by several names.
- A side-by-side preview (original vs monochrome at 24 px) shown to
  the user.
- A short report: source of the original logo, conversion path used,
  lookup verification result, and the commit hash.

Example — Freebuff (double-F redrawn from the installed PNG):

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 16.933 16.933"><defs><style>.ColorScheme-Text {color:#d8dee9}</style></defs><path class="ColorScheme-Text" style="fill:currentColor" d="M2.4 2.4 H14.4 V5.6 H5.6 V7.9 H10.9 V10.5 H5.6 V14.5 H2.4 Z"/><path class="ColorScheme-Text" style="fill:currentColor" d="M7.6 8.3 H13.6 V10.5 H10 V11.7 H12.4 V13.3 H10 V14.5 H7.6 Z"/></svg>
```

## Quality Gates

- [ ] Original logo was displayed and used as the drawing source.
- [ ] File name equals the `.desktop` `Icon=` value exactly.
- [ ] No background plate, no gradient, no second color in the SVG.
- [ ] Canvas is `0 0 16.933 16.933` with the `ColorScheme-Text`
      `currentColor` scheme.
- [ ] Side-by-side render at 24 px is recognizably the same logo.
- [ ] At least one improvement pass if the first render was unclear.
- [ ] Nothing outside the Monochrome-Cosmic repository was modified.
- [ ] GTK lookup for the icon name resolves into the theme.
- [ ] Change committed and pushed; local and GitHub in sync.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Inventing a letter or generic glyph instead of the real logo | Source the original logo first (step 2); invention is failure |
| Adding a dark rounded-square background plate | Glyph only, transparent background (step 4) |
| Literal hex fill on a 24 or 48 canvas | House canvas + `currentColor` scheme (step 4) |
| Suggesting `hicolor` edits or `.desktop` changes | Place the file in the theme; never touch the app |
| Accepting the first AI/trace output | Clean it to paths and run the likeness check (steps 5-6) |
| Copying the file for every alias name | One real file, symlinks for aliases (step 7) |
| Claiming done while COSMIC still shows the old icon | Cache update + process restart + lookup proof (step 8) |

## References

- Project standards: `docs/STANDARDS.md` in the Monochrome-Cosmic
  repository (single source of truth for style decisions).
- Upstream artwork: YAMIS by Dirn,
  https://bitbucket.org/dirn-typo/yet-another-monochrome-icon-set
