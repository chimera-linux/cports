import os

def invoke(pkg):
    patch_done = pkg.statedir / f"{pkg.pkgname}__patch_done"
    if patch_done.is_file():
        return

    pkg.run_step("patch", optional = True)

    patch_done.touch()
