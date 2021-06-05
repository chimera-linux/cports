import os

def invoke(pkg, step):
    configure_done = pkg.statedir / f"{pkg.pkgname}__configure_done"

    if os.path.isfile(configure_done) and (
        not pkg.rparent.force_mode or step != "configure"
    ):
        return

    pkg.run_step("configure", optional = True)

    open(configure_done, "w").close()
