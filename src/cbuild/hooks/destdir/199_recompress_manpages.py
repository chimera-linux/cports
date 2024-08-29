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
    # make this a set to dedup
    files = set()
    manbase = pkg.destdir / "usr/share/man"
    for f in manbase.rglob("*.*"):
        # skip non-files and symlinks to non-files
        # dead links are okay, the .exists() handles it
        if f.exists() and not f.is_file():
            continue
        # capture symlinks
        if f.is_symlink():
            syms.append(f)
        else:
            files.add(str(pkg.chroot_destdir / f.relative_to(pkg.destdir)))
    # now process links
    for f in syms:
        linktgt = f.readlink()
        # if it points outside mandir, also add it for processing
        linkfull = (f.parent / linktgt).resolve()
        if not linkfull.is_relative_to(manbase):
            # now we need to go over each possible subpackage and check...
            # this is very slow but we only do it after filtering things
            # so it will almost never actually happen
            for sp in [*pkg.rparent.subpkg_list, pkg.rparent]:
                spf = (
                    sp.destdir
                    / "usr/share/man"
                    / f.parent.relative_to(manbase)
                    / linktgt
                ).resolve()
                if spf.is_file():
                    files.add(
                        str(sp.chroot_destdir / spf.relative_to(sp.destdir))
                    )
        # always remove link afterwards
        f.unlink()
        f.with_suffix(f"{f.suffix}.gz").symlink_to(f"{linktgt}.gz")
    # and then files
    for f in files:
        # keep to avoid tripping the hardlink detector
        chroot.enter(
            "gzip",
            "-9nf",
            f,
            check=True,
            ro_root=True,
            ro_build=True,
            ro_dest=False,
            unshare_all=True,
        )
