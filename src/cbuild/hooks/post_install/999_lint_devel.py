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


def invoke(pkg):
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
