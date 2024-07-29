from cbuild.core import template


def _invoke_prepkg(pkg):
    p = pkg.rparent.profile()
    crossb = p.arch if p.cross else ""
    prepkg_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_prepkg_done"

    if prepkg_done.is_file() and not pkg.rparent.force_mode:
        return

    template.call_pkg_hooks(pkg, "pre_pkg")

    prepkg_done.touch()


def _do_prepkg(pkg):
    _invoke_prepkg(pkg)

    for apkg, adesc, iif, takef in template.autopkgs:
        # is an explicit package, do not autosplit that
        if pkg.pkgname.endswith(f"-{apkg}"):
            continue

        # explicitly defined, so do not try autosplit
        foundpkg = False
        for sp in pkg.rparent.subpkg_list:
            if sp.pkgname == f"{pkg.pkgname}-{apkg}":
                foundpkg = True
                break
        if foundpkg:
            continue

        ddest = pkg.rparent.destdir_base / f"{pkg.pkgname}-{apkg}-{pkg.pkgver}"

        # destdir does not exist, so skip
        if not ddest.is_dir():
            continue

        spkg = template.Subpackage(f"{pkg.pkgname}-{apkg}", pkg, auto=True)
        # call prepkg hooks for this too
        _invoke_prepkg(spkg)


def invoke(pkg):
    template.call_pkg_hooks(pkg, "init_pkg")

    for sp in pkg.subpkg_list:
        _do_prepkg(sp)

    _do_prepkg(pkg)
