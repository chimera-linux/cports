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

    for apkg, adesc, iif, takef in template.autopkgs:
        if apkg == "static" and not pkg.options["splitstatic"]:
            continue
        if apkg == "udev" and not pkg.options["splitudev"]:
            continue
        if apkg == "doc" and not pkg.options["splitdoc"]:
            continue
        if apkg.startswith("dinit") and not pkg.options["splitdinit"]:
            continue
        if not takef:
            continue
        if pkg.pkgname == iif:
            continue
        if apkg == "dinit-links" and pkg.rparent.pkgname == "dinit-chimera":
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
        sp.destdir.mkdir(parents=True, exist_ok=True)
        takef(sp)
        # remove if empty
        _clean_empty(sp.destdir)
