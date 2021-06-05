import os

def invoke(pkg):
    patch_done = pkg.statedir / f"{pkg.pkgname}__patch_done"
    if os.path.isfile(patch_done):
        return

    pkg.run_step("patch", optional = True)

    open(patch_done, "w").close()
