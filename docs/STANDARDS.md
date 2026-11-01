# Icon Standards — Monochrome-Cosmic

These rules keep every icon in the set visually consistent. They apply
to all new and edited icons. Upstream YAMIS artwork is imported as-is
by `scripts/import_yamis.py`; new icons must follow this document.

## File rules

1. One real file per logo. Names that other applications use for the
   same logo are symlinks to the real file, never copies.
2. File name is exactly the `Icon=` value of the application's
   `.desktop` file (case-sensitive), without extension, plus `.svg`.
3. Icons live in the freedesktop context folder that matches their
   role: `apps/scalable` for applications, `actions/`, `status/`,
   `places/`, `mimetypes/`, `preferences/` for the rest. New context
   folders must be registered in `theme/index.theme`.
4. Never modify the application's own files or `.desktop` entries to
   make an icon fit. All customization lives inside this theme.

## COSMIC specifics

1. COSMIC requests many icons by reverse-DNS name
   (`com.system76.CosmicFiles`, `com.system76.CosmicTerm`, ...).
   Those names are first-class citizens here: every COSMIC app,
   applet, and Settings page name that exists on a stock COSMIC
   install must resolve inside this theme.
2. Applet and panel icons are requested at small sizes and often
   with a `-symbolic` suffix. Alias those names to the fitting
   glyph; a missing symbolic name shows a colorful fallback in the
   panel, which is exactly what this theme exists to prevent.
3. Panel, launcher, and app library cache icons in memory. After
   any change, refresh the icon cache and restart those processes
   (or log out/in) before judging the result on screen.

## Drawing rules

1. Canvas: `viewBox="0 0 16.933 16.933"` (64 x 64), transparent
   background. No background squares, no rounded-corner plates.
2. Single color only: every path uses `class="ColorScheme-Text"` with
   `style="fill:currentColor"`, and the file defines
   `.ColorScheme-Text {color:#d8dee9}`. No gradients, shadows, or
   second colors.
3. The glyph must be the application's real logo, made monochrome:
   - First choice: an existing monochrome source (upstream YAMIS,
     Simple Icons, the vendor's brand page).
   - Otherwise redraw the original logo by hand as SVG paths.
   - AI-generated or PNG-traced results are drafts only: simplify
     them to clean paths before they enter the set.
4. Likeness is total: silhouette, proportions, and signature details
   of the original logo survive. Details that vanish at 24 px are
   simplified, never invented.
5. Verify before committing: render the icon at 16, 24, and 48 px on
   a dark background next to the original logo. It must be
   recognizable as the same app at 24 px.

## Process rules

1. Local folder and GitHub stay in sync: every change ends with a
   commit and a push; pull before starting if GitHub moved.
2. After changing icons, run `gtk-update-icon-cache` on the installed
   theme and restart `cosmic-panel`, `cosmic-launcher`, and
   `cosmic-app-library` (they cache icons in memory), or log out/in.
3. Record every added icon in the commit message; keep this document
   as the single source of truth for style decisions.
