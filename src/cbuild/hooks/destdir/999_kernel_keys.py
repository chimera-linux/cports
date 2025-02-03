from cbuild.core import paths

import shutil


def invoke(pkg):
    db = pkg.destdir / "usr/src"
    # first glob if we have a headers dir, if we have multiple, error
    kdir = None
    for d in db.glob("linux-headers-*"):
        if kdir:
            # this should generally never happen
            pkg.error("multiple kernel headers dirs in one package?")
        kdir = d
    # nothing, just bail
    if not kdir:
        return
    # kernel version
    kver = kdir.name.removeprefix("linux-headers-")
    # first erase whatever was already there
    dpath = paths.keys() / "kernel"
    for f in dpath.glob(f"{kver}-signing_key.*"):
        f.unlink()
    # find if we have signing key stuff in the new kernel
    klist = list((kdir / "certs").glob("signing_key.*"))
    # nothing, bail too
    if len(klist) == 0:
        return
    # else prepare a dir for it
    dpath = paths.keys() / "kernel"
    dpath.mkdir(exist_ok=True, parents=True)
    # and copy it all there
    for sk in klist:
        df = dpath / f"{kver}-{sk.name}"
        shutil.move(sk, df)
