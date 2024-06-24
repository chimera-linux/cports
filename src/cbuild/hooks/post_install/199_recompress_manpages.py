from cbuild.core import chroot


def invoke(pkg):
    for f in (pkg.destdir / "usr/share/man").rglob("*.*"):
        # may be a symlink too
        if not f.is_file():
            continue
        # if a symlink, point it to the right target
        if f.is_symlink():
            linktgt = f.readlink()
            f.unlink()
            f.symlink_to(f"{linktgt}.gz")
        # otherwise compress
        cf = pkg.chroot_destdir / f.relative_to(pkg.destdir)
        chroot.enter(
            "gzip",
            "-9n",
            cf,
            check=True,
            ro_root=True,
            ro_build=True,
            ro_dest=False,
            unshare_all=True,
        )
