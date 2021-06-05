from cbuild.core import template, dependencies

import os

def invoke(pkg):
    prepkg_done = pkg.statedir / f"{pkg.pkgname}__prepkg_done"

    if os.path.isfile(prepkg_done) and not pkg.rparent.force_mode:
        return

    pkg.run_depends = dependencies.get_pkg_depends(pkg, False)
    template.call_pkg_hooks(pkg, "pre_pkg")

    open(prepkg_done, "w").close()
