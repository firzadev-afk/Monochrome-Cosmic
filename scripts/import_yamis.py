import os, shutil, hashlib

SRC = "/tmp/opencode/yamis-src"
OLD = os.path.expanduser("~/.local/share/icons/YAMIS-Cosmic")
DST = "/home/alfarez/Monochrome-Cosmic/theme"

CONTEXTS = ["actions", "apps", "categories", "devices", "emblems",
            "mimetypes", "places", "preferences", "status"]
SKIP_DIRS = {"scalable-outlined"}  # varian mimetype alternatif, dirampingkan

def content_hash(path):
    with open(path, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()

stats = {"real": 0, "alias": 0, "skipped": 0}
for ctx in CONTEXTS:
    src_ctx = os.path.join(SRC, ctx)
    if not os.path.isdir(src_ctx):
        continue
    # kelompokkan per direktori berdasarkan isi
    for root, dirs, files in os.walk(src_ctx):
        rel_dir = os.path.relpath(root, SRC)
        if any(part in SKIP_DIRS for part in rel_dir.split(os.sep)):
            stats["skipped"] += len(files)
            continue
        groups = {}
        for f in files:
            p = os.path.join(root, f)
            try:
                h = content_hash(p)
            except Exception:
                continue
            groups.setdefault(h, []).append(f)
        out_dir = os.path.join(DST, rel_dir)
        os.makedirs(out_dir, exist_ok=True)
        for h, names in groups.items():
            def rank(name):
                is_link = os.path.islink(os.path.join(root, name))
                return (1 if is_link else 0,          # file asli dulu
                        0 if "." in name[:-4] else 1,  # nama reverse-DNS dulu
                        len(name), name.lower())
            canonical = sorted(names, key=rank)[0]
            shutil.copyfile(os.path.join(root, canonical),
                            os.path.join(out_dir, canonical))
            stats["real"] += 1
            for alias in names:
                if alias == canonical:
                    continue
                dest = os.path.join(out_dir, alias)
                if os.path.lexists(dest):
                    os.unlink(dest)
                os.symlink(canonical, dest)
                stats["alias"] += 1
print(stats)

# overlay icon custom project lama (hasil kerja firzadev-afk)
overlay = [
    "apps/scalable/ai.storyteller.deckcraft.svg",
    "apps/scalable/ai.storyteller.gridcraft.svg",
    "apps/scalable/ai.storyteller.pdfcraft.svg",
    "apps/scalable/ai.storyteller.wordcraft.svg",
    "apps/scalable/freebuff.svg",
    "apps/scalable/freebuff-0.0.192-linux-x86_64.svg",
    "apps/scalable/stably-orca.svg",
    "apps/scalable/zcode.svg",
    "apps/scalable/com.system76.CosmicAppletNotifications-symbolic.svg",
    "apps/scalable/com.system76.CosmicAppletStatusArea.svg",
]
link_overlay = {
    "apps/scalable/ai.opencode.desktop.svg": "opencode.svg",
    "apps/scalable/com.system76.CosmicAppLibrary.svg": "dev.xarbit.appgrid.svg",
    "apps/scalable/com.system76.CosmicAppList.svg": "dev.xarbit.appgrid.svg",
    "apps/scalable/com.system76.CosmicPanelAppButton.svg": "dev.xarbit.appgrid.svg",
    "apps/scalable/com.system76.CosmicPlayer.svg": "io.github.celluloid_player.Celluloid.svg",
    "apps/scalable/com.system76.CosmicLauncher.svg": "system-search.svg",
    "apps/scalable/com.system76.CosmicPanelLauncherButton.svg": "system-search.svg",
}
for rel in overlay:
    src = os.path.join(OLD, rel)
    dest = os.path.join(DST, rel)
    if os.path.lexists(dest):
        os.unlink(dest)
    shutil.copyfile(src, dest)
    print("overlay", rel)
for rel, target in link_overlay.items():
    dest = os.path.join(DST, rel)
    if os.path.lexists(dest):
        os.unlink(dest)
    os.symlink(target, dest)
    print("overlay-link", rel, "->", target)

# alias symlink tambahan dari project lama (daftar di commit ccd55c0)
extra_aliases = [
    "applications-system-symbolic", "com.ktechpit.whatsie", "shelly-tray",
    "flatpak-symbolic", "input-keyboard-symbolic", "mark-location-symbolic",
    "com.system76.CosmicAppletAudio-symbolic", "com.system76.CosmicAppletBattery-symbolic",
    "com.system76.CosmicAppletBluetooth-symbolic", "com.system76.CosmicAppletInputSources-symbolic",
    "com.system76.CosmicAppletMinimize", "com.system76.CosmicAppletNetwork-symbolic",
    "com.system76.CosmicAppletPower-symbolic", "com.system76.CosmicAppletTiling-symbolic",
    "com.system76.CosmicAppletTime-symbolic", "com.system76.CosmicAppletWorkspaces",
    "com.system76.CosmicInitialSetup", "com.system76.CosmicMonitor",
    "com.system76.CosmicPanelWorkspacesButton", "com.system76.CosmicViewer",
    "com.system76.CosmicWorkspaces",
]
apps_dst = os.path.join(DST, "apps/scalable")
for name in extra_aliases:
    src = os.path.join(OLD, "apps/scalable", name + ".svg")
    dest = os.path.join(apps_dst, name + ".svg")
    if not os.path.islink(src):
        print("BUKAN symlink di lama:", name)
        continue
    if os.path.lexists(dest):
        os.unlink(dest)
    os.symlink(os.readlink(src), dest)
    print("alias", name, "->", os.readlink(src))

# Lapisan terakhir: file khas fork COSMIC (harpoonwithaz) yang tidak ada
# di upstream Bitbucket. Salin hanya yang belum ada di theme baru.
added = 0
for ctx in CONTEXTS:
    old_ctx = os.path.join(OLD, ctx)
    if not os.path.isdir(old_ctx):
        continue
    for root, dirs, files in os.walk(old_ctx):
        rel_dir = os.path.relpath(root, OLD)
        if "scalable-outlined" in rel_dir.split(os.sep):
            continue
        for f in files:
            src = os.path.join(root, f)
            dest = os.path.join(DST, rel_dir, f)
            if os.path.lexists(dest):
                continue
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if os.path.islink(src):
                os.symlink(os.readlink(src), dest)
            else:
                shutil.copyfile(src, dest)
            added += 1
print(f"file fork ditambahkan: {added}")
