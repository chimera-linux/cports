def strip(pkg, *args):
    strip_path = "/usr/bin/" + pkg.rparent.get_tool("STRIP")

    if len(args) == 0:
        return

    try:
        pkg.rparent.do(
            strip_path,
            "--strip-unneeded",
            "--remove-section=.comment",
            "--keep-section=.gnu_debuglink",
            *map(lambda v: pkg.chroot_destdir / v, args),
        )
    except Exception:
        pkg.error("failed to strip one of inputs")


def split_debug(pkg, *args):
    if not pkg.rparent.options["debug"] or not pkg.rparent.build_dbg:
        return

    for path in args:
        dfile = pkg.destdir / "usr/lib/debug" / path
        cfile = pkg.chroot_destdir / "usr/lib/debug" / path

        dfile.parent.mkdir(parents=True, exist_ok=True)
        try:
            pkg.rparent.do(
                pkg.rparent.get_tool("OBJCOPY"),
                "--only-keep-debug",
                pkg.chroot_destdir / path,
                cfile,
            )
        except Exception:
            pkg.error(f"failed to create dbg file for {path}")

        dfile.chmod(0o644)


def attach_debug(pkg, *args):
    if not pkg.rparent.options["debug"] or not pkg.rparent.build_dbg:
        return

    for path in args:
        cfile = pkg.chroot_destdir / "usr/lib/debug" / path
        try:
            pkg.rparent.do(
                pkg.rparent.get_tool("OBJCOPY"),
                f"--add-gnu-debuglink={cfile}",
                pkg.chroot_destdir / path,
            )
        except Exception:
            pkg.error(f"failed to attach debug link to {path}")


def strip_attach(pkg, *args):
    split_debug(pkg, *args)
    strip(pkg, *args)
    attach_debug(pkg, *args)
