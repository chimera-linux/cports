from cbuild.core import paths

import os

def invoke(pkg):
    cfgl = []

    # for stage 0 we have nowhere to put the config and we don't care
    if pkg.stage == 0:
        return

    # explicitly handle linker and lto threads
    cfgl.append(f"-Wl,--threads={pkg.link_threads}")
    if pkg.options["lto"]:
        cfgl.append(f"-flto-jobs={pkg.lto_jobs}")

    # write it out
    cp = paths.bldroot() / "etc/clang"
    cp.mkdir(parents = True, exist_ok = True)
    with open(cp / "clang.cfg", "w") as outf:
        for opt in cfgl:
            outf.write(opt)
            outf.write("\n")
