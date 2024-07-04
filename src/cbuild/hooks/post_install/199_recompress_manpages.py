from cbuild.core import chroot


def invoke(pkg):
    # don't run for early stages (stage0 can't at all because no
    # chroot, stage1 would just waste time on this pointlessly
    if pkg.stage < 2:
        return
    # otherwise go over everything; do 2 passes in order to make sure
    # all symlinks to files remain valid while we work on them, do them
    # first to safely retarget, then process files
    syms = []
    files = []
    for f in (pkg.destdir / "usr/share/man").rglob("*.*"):
        # skip non-files and symlinks to non-files
        # dead links are okay, the .exists() handles it
        if f.exists() and not f.is_file():
            continue
        # capture symlinks
        if f.is_symlink():
            syms.append(f)
        else:
            files.append(f)
    # now process links
    for f in syms:
        linktgt = f.readlink()
        f.unlink()
        f.with_suffix(f"{f.suffix}.gz").symlink_to(f"{linktgt}.gz")
    # and then files
    for f in files:
        rp = f.relative_to(pkg.destdir)
        # keep to avoid tripping the hardlink detector
        chroot.enter(
            "gzip",
            "-9nk",
            pkg.chroot_destdir / rp,
            check=True,
            ro_root=True,
            ro_build=True,
            ro_dest=False,
            unshare_all=True,
        )
        (pkg.destdir / rp).unlink()
