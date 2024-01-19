def invoke(pkg):
    # does not apply
    if pkg.pkgname == "base-files" or pkg.pkgname == "base-kernel":
        return

    # gcompat is allowed to have them
    if pkg.pkgname == "gcompat":
        return

    lintfail = False
    dirempty = True

    # toplevel must only contain directories
    for f in pkg.destdir.glob("*"):
        dirempty = False
        rf = f.relative_to(pkg.destdir)
        if f.is_symlink() or not f.is_dir():
            pkg.log_red(f"forbidden file '{rf}'")
            lintfail = True

    # certain paths must not exist, they are symlinks or in base-files
    # or just outright forbidden (like wordsize specific lib symlinks)
    for d in [
        "bin",
        "lib",
        "lib32",
        "lib64",
        "sbin",
        "usr/sbin",
        "usr/lib32",
        "usr/lib64",
        "var/run",
        "usr/local",
        "usr/lib/locale",
        "usr/share/mime/XMLnamespaces",
        "usr/share/mime/aliases",
        "usr/share/mime/generic-icons",
        "usr/share/mime/globs",
        "usr/share/mime/globs2",
        "usr/share/mime/icons",
        "usr/share/mime/magic",
        "usr/share/mime/mime.cache",
        "usr/share/mime/subclasses",
        "usr/share/mime/treemagic",
        "usr/share/mime/types",
        "usr/share/mime/version",
    ]:
        if (pkg.destdir / d).exists():
            pkg.log_red(f"forbidden path '{d}'")
            lintfail = True

    allowpaths = {
        "boot": True,
        "etc": True,
        "opt": True,
        "usr": True,
        "var": True,
    }

    # toplevel must only contain allowed paths
    for f in pkg.destdir.glob("*"):
        rf = f.relative_to(pkg.destdir)
        if f.name not in allowpaths:
            pkg.log_red(f"forbidden directory '{rf}'")
            lintfail = True

    if dirempty and pkg.build_style != "meta" and not pkg.options["empty"]:
        pkg.log_red("empty non-meta packages must be marked as such")
        lintfail = True
    elif not dirempty and pkg.options["empty"]:
        pkg.log_red("package marked empty but not actually empty")
        lintfail = True

    # stuff in /etc that should go in /usr/lib
    for d in [
        "modprobe.d",
        "sysctl.d",
        "tmpfiles.d",
        "udev/rules.d",
        "udev/hwdb.d",
    ]:
        if d == "modprobe.d" and pkg.pkgname == "kmod":
            continue
        if (pkg.destdir / "etc" / d).exists():
            pkg.log_red(f"{d} should go in /usr/lib, not /etc")
            lintfail = True

    # stuff in /etc that should go in /usr/share
    for d in [
        "bash_completion.d",
        "dbus-1/session.d",
        "dbus-1/system.d",
        "fonts/conf.avail",
        "polkit-1/rules.d",
        "X11/xorg.conf.d",
        "gconf/schemas",
    ]:
        if (pkg.destdir / "etc" / d).exists():
            pkg.log_red(f"{d} should go in /usr/share, not /etc")
            lintfail = True

    # stuff in /usr that should go in /usr/share
    for d in ["man", "doc", "dict"]:
        if (pkg.destdir / "usr" / d).exists():
            pkg.log_red(f"{d} should go in /usr/share, not /usr")
            lintfail = True

    # python stuff that should not be in site-packages
    for d in (pkg.destdir / "usr/lib").glob("python*"):
        sp = d / "site-packages"
        if not sp.is_dir():
            continue
        # none of the stuff that would go in absolute prefix
        for d in [
            "bin",
            "etc",
            "lib",
            "lib32",
            "lib64",
            "opt",
            "sbin",
            "share",
            "usr",
            "var",
        ]:
            if (sp / d).exists():
                pkg.log_red(f"{d} found in Python site-packages")
                lintfail = True

    if lintfail:
        pkg.error("package lint failed")
