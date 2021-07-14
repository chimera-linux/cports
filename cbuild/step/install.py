from cbuild.core import template, dependencies, scanelf

import os

def invoke(pkg, subpkg_mode):
    crossb = pkg.rparent.cross_build if pkg.rparent.cross_build else ""
    install_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_install_done"

    if not subpkg_mode:
        template.call_pkg_hooks(pkg, "init_install")
        template.run_pkg_func(pkg, "init_install")

        if not install_done.is_file() or pkg.force_mode:
            os.makedirs(pkg.destdir, exist_ok = True)
            pkg.run_step("install", skip_post = True)
            install_done.touch()
        return

    subpkg_install_done = pkg.statedir / f"{pkg.pkgname}_{crossb}_subpkg_install_done"

    if subpkg_install_done.is_file():
        scanelf.scan(pkg, pkg.rparent.current_elfs)
        return

    # this is a real subpackage
    if pkg.parent:
        os.makedirs(pkg.destdir, exist_ok = True)
        if pkg.pkg_install:
            template.call_pkg_hooks(pkg, "pre_install")
            template.run_pkg_func(pkg, "pkg_install", on_subpkg = True)

    pkg.run_depends = list(pkg.depends)

    scanelf.scan(pkg, pkg.rparent.current_elfs)

    template.call_pkg_hooks(pkg, "post_install")

    subpkg_install_done.touch()
