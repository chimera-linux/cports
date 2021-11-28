def invoke(pkg):
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

    if not pkg.pkgname.endswith("-static"):
        for v in pkg.destdir.rglob("usr/lib/*.a"):
            pkg.log_warn("static libraries should be in the -static package")
            break

    for v in pkg.destdir.rglob("usr/lib/*.so"):
        pkg.log_warn(".so symlinks should be in the -devel package")
        break

    for v in pkg.destdir.rglob("usr/bin/*-config"):
        pkg.log_warn("*-config tools should be in the -devel package")
        break
