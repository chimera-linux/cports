def _lint_static(pkg):
    if pkg.pkgname.endswith("-static"):
        return True

    for v in (pkg.destdir / "usr/lib").rglob("*.a"):
        allow = not pkg.rparent.options["lto"] or pkg.options["ltostrip"]
        if not allow or pkg.options["splitstatic"]:
            pkg.log_red("static libraries should be in the -static package")
            return False
        else:
            pkg.log_warn(
                "static libraries should usually be in the -static package"
            )
            return True

    return True


def _lint_license(pkg):
    if not pkg._license_install or not pkg.options["distlicense"]:
        return

    has_license = False
    lpath = pkg.destdir / "usr/share/licenses"
    if not lpath.is_dir():
        # the license may have been split into docpkg
        lpath = (
            pkg.destdir.parent
            / f"{pkg.pkgname}-doc-{pkg.pkgver}/usr/share/licenses"
        )
    if lpath.is_dir():
        for f in lpath.iterdir():
            has_license = True
            break

    if not has_license:
        pkg.error("license installation necessary but no license installed")


def _lint_devel(pkg):
    # lint for LTOed static stuff first, regardless of -devel
    if pkg.options["lintstatic"] and not _lint_static(pkg):
        pkg.error("package lint failed")

    if pkg.pkgname.endswith("-devel"):
        return

    for sp in pkg.rparent.subpkg_list:
        if sp.pkgname.endswith("-devel"):
            break
    else:
        return

    badpaths = {
        "usr/include": True,
        "usr/lib/cmake": True,
        "usr/lib/glade/modules": True,
        "usr/lib/pkgconfig": True,
        "usr/share/pkgconfig": True,
        "usr/share/vala/vapi": True,
        "usr/share/gir-1.0": True,
        "usr/share/aclocal": True,
        "usr/share/gettext": True,
        "usr/share/cmake": True,
        "usr/share/glade/catalogs": True,
    }

    for v in pkg.destdir.rglob("*"):
        if v.is_symlink() or not v.is_dir():
            continue
        v = str(v.relative_to(pkg.destdir))
        if v in badpaths:
            pkg.log_warn(f"{v} should be in the -devel package")

    for v in pkg.destdir.rglob("usr/lib/*.so"):
        pkg.log_warn(".so symlinks should be in the -devel package")
        break

    for v in pkg.destdir.rglob("usr/bin/*-config"):
        pkg.log_warn("*-config tools should be in the -devel package")
        break


def invoke(pkg):
    _lint_devel(pkg)
    _lint_license(pkg)

    # does not apply
    if pkg.pkgname == "base-files" or pkg.pkgname == "base-kernel":
        return

    # gcompat and bash-completion is allowed to have them
    if pkg.pkgname in ["bash-completion", "gcompat"]:
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
        "usr/build-1",
        "usr/cgi-bin",
        "usr/etc",
        "usr/sbin",
        "usr/lib32",
        "usr/lib64",
        "var/run",
        "usr/local",
        "usr/lib/locale",
        "usr/lib/systemd/system",
        "usr/lib/systemd/user",
        "usr/share/glib-2.0/schemas/gschemas.compiled",
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
        "usr/tests",
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

    if (
        dirempty
        and pkg.build_style != "meta"
        and not pkg.options["empty"]
        and not pkg.autopkg
    ):
        pkg.log_red("empty non-meta packages must be marked as such")
        lintfail = True
    elif not dirempty and pkg.options["empty"] and not pkg.autopkg:
        pkg.log_red("package marked empty but not actually empty")
        lintfail = True

    # stuff in /etc that should go in /usr/lib
    for d in [
        "kernel.d",
        "modprobe.d",
        "pam.d",
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

    if (
        pkg.pkgname != "fish-shell"
        and (pkg.destdir / "usr/share/fish/completions").exists()
    ):
        pkg.log_red(
            "fish completions should go in usr/share/fish/vendor_completions.d, not usr/share/fish/completions"
        )
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
