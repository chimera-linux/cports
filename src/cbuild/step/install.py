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
        template.call_pkg_hooks(pkg, "pre_install")
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
            pkg.log_warn(f"removed empty directory: {pr}")
        dpath.rmdir()
        return True

    return False


def _split_auto(pkg):
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
        _clean_empty(sp, sp.destdir, True)


def invoke(pkg, step):
    p = pkg.profile()
    crossb = p.arch if p.cross else ""
    install_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_install_done"

    # scan for ELF information after subpackages are split up
    # but before post_install hooks (done by the install step)
    pkg.current_elfs = {}

    template.call_pkg_hooks(pkg, "init_install")
    template.run_pkg_func(pkg, "init_install")

    if install_done.is_file() and (not pkg.force_mode or step != "install"):
        # when repeating, ensure to at least scan the ELF info...
        for sp in pkg.subpkg_list:
            scanelf.scan(sp, pkg.current_elfs)
        scanelf.scan(pkg, pkg.current_elfs)
        return

    if pkg.destdir.is_dir():
        shutil.rmtree(pkg.destdir, onerror=_remove_ro)
    pkg.destdir.mkdir(parents=True, exist_ok=True)
    pkg.run_step("install", skip_post=True)

    pkg.install_done = True

    for sp in pkg.subpkg_list:
        _invoke_subpkg(sp)
        scanelf.scan(sp, pkg.current_elfs)
        template.call_pkg_hooks(sp, "post_install")
        _split_auto(sp)
        if not sp.options["keepempty"]:
            _clean_empty(sp, sp.destdir, False)

    scanelf.scan(pkg, pkg.current_elfs)
    template.call_pkg_hooks(pkg, "post_install")
    _split_auto(pkg)
    _clean_empty(pkg, pkg.destdir, False)

    install_done.touch()
