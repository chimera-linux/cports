def _lint_static_cfi(pkg):
    if pkg.rparent.has_hardening("cfi") and not pkg.options["ltostrip"]:
        pkg.log_red("CFI enabled on a template with static libraries")
        return False

    return True


def _lint_static(pkg):
    if pkg.pkgname.endswith("-static"):
        return _lint_static_cfi(pkg)

    for v in (pkg.destdir / "usr/lib").rglob("*.a"):
        allow = not pkg.rparent.options["lto"] or pkg.options["ltostrip"]
        if not allow or pkg.options["splitstatic"]:
            pkg.log_red("static libraries should be in the -static package")
            return False
        else:
            pkg.log_warn(
                "static libraries should usually be in the -static package"
            )
            return _lint_static_cfi(pkg)

    return True


def _lint_license(pkg):
    if not pkg._license_install or not pkg.options["distlicense"]:
        return

    has_license = False
    lpath = pkg.destdir / "usr/share/licenses"
    if not lpath.is_dir():
        # the license may have been split into docpkg
        lpath = pkg.destdir.parent / f"{pkg.pkgname}-doc/usr/share/licenses"
    if lpath.is_dir():
        for f in lpath.iterdir():
            has_license = True
            break

    if not has_license:
        pkg.error(
            "license installation necessary but no license installed",
            hint="install it using self.install_license in the install phase",
        )


def _lint_bashcomp(pkg):
    if (pkg.destdir / "etc/bash_completion.d").is_dir():
        pkg.error(
            "/etc/bash_completion.d found, should be /usr/share/bash-completion"
        )

    for p in (pkg.destdir / "usr/share/bash-completion/completions").iterdir():
        if not (pkg.parent.destdir / "usr/bin" / p.name).exists():
            pkg.error(f"bash completion '{p.name}' has no matching command")


def _lint_zshcomp(pkg):
    for p in (pkg.destdir / "usr/share/zsh/site-functions").iterdir():
        if not p.name.startswith("_"):
            continue
        if not (
            pkg.parent.destdir / "usr/bin" / p.name.removeprefix("_")
        ).exists():
            pkg.error(f"zsh completion '{p.name}' has no matching command")


def _lint_fishcomp(pkg):
    if (pkg.destdir / "usr/share/fish/completions").exists():
        pkg.error(
            "fish completions need to go in usr/share/fish/vendor_completions.d, not usr/share/fish/completions"
        )

    for p in (pkg.destdir / "usr/share/fish/vendor_completions.d").iterdir():
        if not (
            pkg.parent.destdir / "usr/bin" / p.name.removesuffix(".fish")
        ).exists():
            pkg.error(f"fish completion '{p.name}' has no matching command")


def _lint_nucomp(pkg):
    # we cannot lint command existence here because the nushell path is
    # more generic (it does not contain just per-command completions)
    pass


def _lint_comp(pkg):
    if not pkg.options["lintcomp"]:
        return
    if pkg.pkgname.endswith("-bashcomp"):
        _lint_bashcomp(pkg)
    elif pkg.pkgname.endswith("-zshcomp"):
        _lint_zshcomp(pkg)
    elif pkg.pkgname.endswith("-fishcomp"):
        _lint_fishcomp(pkg)
    elif pkg.pkgname.endswith("-nucomp"):
        _lint_nucomp(pkg)


def _lint_devel(pkg):
    # lint for LTOed static stuff first, regardless of -devel
    if pkg.options["lintstatic"] and not _lint_static(pkg):
        pkg.error(
            "package lint failed",
            hint="maybe you forgot to create a -devel subpackage?",
        )

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
    _lint_comp(pkg)

    # does not apply
    if pkg.pkgname == "base-files" or pkg.pkgname == "base-kernel":
        return

    lintfail = False
    dirempty = True

    allowpaths = {
        "boot": True,
        "etc": True,
        "usr": True,
    }

    # toplevel must only contain allowed paths
    # additionally, it must only contain directories
    for f in pkg.destdir.glob("*"):
        dirempty = False
        rf = f.relative_to(pkg.destdir)
        if f.name not in allowpaths:
            pkg.log_red(f"forbidden directory '{rf}'")
            lintfail = True
            continue
        if f.is_symlink() or not f.is_dir():
            pkg.log_red(f"forbidden file '{rf}'")
            lintfail = True

    # certain /usr paths must not exist, they are symlinks or in base-files
    # or just outright forbidden (like wordsize specific lib symlinks)
    for d in [
        "build-1",
        "cgi-bin",
        "etc",
        "sbin",
        "lib32",
        "lib64",
        "local",
        "lib/installed-tests",
        "lib/locale",
        "lib/systemd/system",
        "lib/systemd/user",
        "libexec/installed-tests",
        "share/glib-2.0/schemas/gschemas.compiled",
        "share/installed-tests",
        "share/mime/XMLnamespaces",
        "share/mime/aliases",
        "share/mime/generic-icons",
        "share/mime/globs",
        "share/mime/globs2",
        "share/mime/icons",
        "share/mime/magic",
        "share/mime/mime.cache",
        "share/mime/subclasses",
        "share/mime/treemagic",
        "share/mime/types",
        "share/mime/version",
        "tests",
    ]:
        if (pkg.destdir / "usr" / d).exists():
            pkg.log_red(f"forbidden path '/usr/{d}'")
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

    # kernel signing stuff, reject explicitly
    for d in (pkg.destdir / "usr/src").glob("linux-headers-*/certs"):
        for f in d.glob("signing_key.*"):
            pkg.log_red(f"{d} found in packaged kernel headers")

    if lintfail:
        pkg.error("package lint failed")
