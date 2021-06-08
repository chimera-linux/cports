from cbuild.core import template, dependencies

import os

def invoke(pkg, subpkg_mode):
    install_done = pkg.statedir / f"{pkg.pkgname}__install_done"

    if not subpkg_mode:
        if not install_done.is_file() or pkg.force_mode:
            os.makedirs(pkg.destdir, exist_ok = True)
            pkg.run_step("install", skip_post = True)
            install_done.touch()
        return

    subpkg_install_done = pkg.statedir / f"{pkg.pkgname}__subpkg_install_done"

    if subpkg_install_done.is_file():
        return

    # this is a real subpackage
    if pkg.parent:
        os.makedirs(pkg.destdir, exist_ok = True)
        if hasattr(pkg, "pkg_install"):
            template.call_pkg_hooks(pkg, "pre_install")
            template.run_pkg_func(pkg, "pkg_install", on_subpkg = True)

    pkg.run_depends = list(pkg.depends)
    template.call_pkg_hooks(pkg, "post_install")

    subpkg_install_done.touch()
