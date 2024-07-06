def strip(pkg, path):
    strip_path = "/usr/bin/" + pkg.rparent.get_tool("STRIP")

    relp = path.relative_to(pkg.destdir)
    cfile = str(pkg.chroot_destdir / relp)

    try:
        pkg.rparent.do(
            strip_path,
            "--strip-unneeded",
            "--remove-section=.comment",
            "--keep-section=.gnu_debuglink",
            cfile,
        )
    except Exception:
        pkg.error(f"failed to strip {relp}")

    return relp


def split_debug(pkg, path):
    if not pkg.rparent.options["debug"] or not pkg.rparent.build_dbg:
        return

    relp = path.relative_to(pkg.destdir)

    dfile = pkg.destdir / "usr/lib/debug" / relp
    cfile = pkg.chroot_destdir / "usr/lib/debug" / relp

    dfile.parent.mkdir(parents=True, exist_ok=True)
    try:
        pkg.rparent.do(
            pkg.rparent.get_tool("OBJCOPY"),
            "--only-keep-debug",
            pkg.chroot_destdir / relp,
            cfile,
        )
    except Exception:
        pkg.error(f"failed to create dbg file for {relp}")

    dfile.chmod(0o644)


def attach_debug(pkg, path):
    if not pkg.rparent.options["debug"] or not pkg.rparent.build_dbg:
        return

    relp = path.relative_to(pkg.destdir)

    cfile = pkg.chroot_destdir / "usr/lib/debug" / relp
    try:
        pkg.rparent.do(
            pkg.rparent.get_tool("OBJCOPY"),
            f"--add-gnu-debuglink={cfile}",
            pkg.chroot_destdir / relp,
        )
    except Exception:
        pkg.error(f"failed to attach debug link to {relp}")


def strip_attach(pkg, path):
    split_debug(pkg, path)
    rv = strip(pkg, path)
    attach_debug(pkg, path)
    return rv
