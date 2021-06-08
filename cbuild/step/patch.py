from cbuild.core import template

import os

def invoke(pkg):
    patch_done = pkg.statedir / f"{pkg.pkgname}__patch_done"

    template.call_pkg_hooks(pkg, "init_patch")
    template.run_pkg_func(pkg, "init_patch")

    if patch_done.is_file():
        return

    pkg.run_step("patch", optional = True)

    patch_done.touch()
