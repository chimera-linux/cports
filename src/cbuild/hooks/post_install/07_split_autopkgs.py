from cbuild.core import template

def _clean_empty(dpath):
    empty = True
    for f in dpath.iterdir():
        if f.is_dir() and not f.is_symlink():
            if not _clean_empty(f):
                empty = False
        else:
            empty = False

    if empty:
        dpath.rmdir()
        return True

    return False

def invoke(pkg):
    if not pkg.options["autosplit"]:
        return

    # handle static specially
    if pkg.options["splitstatic"] and pkg.pkgname.endswith("-devel"):
        foundpkg = False
        bn = pkg.pkgname.removesuffix("-devel") + "-static"
        for sp in pkg.rparent.subpkg_list:
            if sp.pkgname == bn:
                foundpkg = True
                break
        if not foundpkg:
            sp = template.Subpackage(bn, pkg)
            sp.destdir.mkdir(parents = True, exist_ok = True)
            for f in (pkg.destdir / "usr/lib").rglob("*.a"):
                sp.take(str(f.relative_to(pkg.destdir)))
            _clean_empty(sp.destdir)

    for apkg, adesc, iif, takef, excl in template.autopkgs:
        if not takef:
            continue
        if excl and pkg.pkgname in excl:
            continue
        if pkg.pkgname == iif:
            continue
        if pkg.pkgname.endswith(f"-{apkg}"):
            continue

        foundpkg = False
        for sp in pkg.rparent.subpkg_list:
            if sp.pkgname == f"{pkg.pkgname}-{apkg}":
                foundpkg = True
                break
        if foundpkg:
            continue

        sp = template.Subpackage(f"{pkg.pkgname}-{apkg}", pkg)
        sp.destdir.mkdir(parents = True, exist_ok = True)
        takef(sp)
        # remove if empty
        _clean_empty(sp.destdir)
