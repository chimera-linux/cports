import os

def invoke(pkg, step):
    build_done = pkg.statedir / f"{pkg.pkgname}__build_done"

    if os.path.isfile(build_done) and (
        not pkg.rparent.force_mode or step != "build"
    ):
        return

    pkg.run_step("build", optional = True)

    open(build_done, "w").close()
