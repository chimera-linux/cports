from cbuild.core import logger, paths
from cbuild.apk import cli

import time
import shutil

def check_stage():
    return True

def clear(arch, signkey):
    repop = paths.repository()
    log = logger.get()

    log.out(f"Clearing staged {arch} repos for {repop}...")

    if not check_stage():
        return

    # FIXME: compute from git if possible
    epoch = int(time.time())

    # we list() to really glob it before doing any changes
    for d in list(repop.rglob(".stage")):
        # do not clear a stage that has nothing in it
        if not (d / arch / "APKINDEX.tar.gz").is_file():
            continue
        # if the actual repo does not exist, just migrate stage
        ad = d.parent / arch
        d = d / arch
        try:
            ad.rmdir()
        except:
            pass
        # just migrate if possible, easier this way
        if not ad.is_dir():
            log.out(f"Migrating stage from {d} to {ad}...")
            d.rename(ad)
            continue
        # else merge the directories
        log.out(f"Merging stage from {d} to {ad}...")
        for f in d.glob("*.apk"):
            f.rename(ad / f.name)
        # clear the stage index, we won't need it
        (d / "APKINDEX.tar.gz").unlink()
        # try removing the stage dir, but keep it if there is still stuff in it
        try:
            d.rmdir()
            d.parent.rmdir()
        except:
            pass
        # finally reindex
        log.out(f"Rebuilding index for {ad}...")
        cli.build_index(ad, epoch, signkey)
