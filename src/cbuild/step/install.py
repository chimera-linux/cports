from cbuild.core import template, scanelf

import os
import shutil
import stat


def _remove_ro(f, path, _):
    os.chmod(path, stat.S_IWRITE)
    f(path)


def _invoke_subpkg(pkg):
    if pkg.destdir.is_dir():
        shutil.rmtree(pkg.destdir, onerror=_remove_ro)
    pkg.destdir.mkdir(parents=True, exist_ok=True)
    if pkg.pkg_install:
        template.run_pkg_func(pkg, "pkg_install", on_subpkg=True)
    # get own licenses by default
    pkg.take(f"usr/share/licenses/{pkg.pkgname}", missing_ok=True)


def _clean_empty(pkg, dpath, auto):
    empty = True

    for f in dpath.iterdir():
        if f.is_dir() and not f.is_symlink():
            if not _clean_empty(pkg, f, auto):
                empty = False
        else:
            empty = False

    if empty and (auto or dpath != pkg.destdir):
        if not auto:
            pr = dpath.relative_to(pkg.destdir)
            pkg.logger.out_plain(f"  \f[orange]clean empty:\f[] {pr}")
        dpath.rmdir()
        return True

    return False


def _split_auto(pkg, done):
    pkg.rparent.subpkg_all.append(pkg)

    pkg.log("\f[cyan]splitting\f[]\f[bold] autopackages...")

    for apkg, adesc, iif, takef in template.autopkgs:
        if takef and not pkg.options["autosplit"]:
            continue
        if apkg == "static" and not pkg.options["splitstatic"]:
            continue
        if apkg == "udev" and not pkg.options["splitudev"]:
            continue
        if apkg == "doc" and not pkg.options["splitdoc"]:
            continue
        if apkg.startswith("dinit") and not pkg.options["splitdinit"]:
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

        sp = template.Subpackage(
            f"{pkg.pkgname}-{apkg}", pkg, pkg.pkgdesc, pkg.subdesc, auto=adesc
        )

        # only take if we're not repeating
        if not done and takef:
            sp.destdir.mkdir(parents=True, exist_ok=True)
            takef(sp)
            # remove if empty
            _clean_empty(sp, sp.destdir, True)

        # now save it only if the destdir still exists
        if sp.destdir.is_dir():
            pkg.rparent.subpkg_all.append(sp)

    # finally clean up empty if needed
    if not done and not pkg.options["keepempty"]:
        _clean_empty(pkg, pkg.destdir, False)


def invoke(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    install_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_install_done"

    # scan for ELF information after subpackages are split up
    # but before post_install hooks (done by the install step)
    pkg.current_elfs = {}

    # to be populated with Subpackages for current and later use
    pkg.subpkg_all = []

    template.run_pkg_func(pkg, "init_install")

    if install_done.is_file() and (not pkg.force_mode or step != "install"):
        # when repeating, ensure to at least scan the ELF info...
        for sp in pkg.subpkg_list:
            scanelf.scan(sp, pkg.current_elfs)
            _split_auto(sp, True)
        scanelf.scan(pkg, pkg.current_elfs)
        _split_auto(pkg, True)
        return

    if pkg.destdir.is_dir():
        shutil.rmtree(pkg.destdir, onerror=_remove_ro)
    pkg.destdir.mkdir(parents=True, exist_ok=True)

    template.run_pkg_func(pkg, "pre_install")
    template.run_pkg_func(pkg, "install")
    template.run_pkg_func(pkg, "post_install")

    pkg.install_done = True

    for sp in pkg.subpkg_list:
        _invoke_subpkg(sp)
        scanelf.scan(sp, pkg.current_elfs)
        template.call_pkg_hooks(sp, "destdir")

    scanelf.scan(pkg, pkg.current_elfs)
    template.call_pkg_hooks(pkg, "destdir")

    # do the splitting at the end to respect e.g. dbg packages
    # empty dir cleaning must be done *after* splitting!
    for sp in pkg.subpkg_list:
        _split_auto(sp, False)
    _split_auto(pkg, False)

    install_done.touch()
