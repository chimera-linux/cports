from cbuild.core import logger, paths

import os
import time
import fcntl
from contextlib import contextmanager

no_lock = False


def set_nolock(nolock):
    global no_lock
    no_lock = nolock


@contextmanager
def lock(path, pkg=None):
    if no_lock:
        yield -1
        return
    fd = os.open(path, os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
    while True:
        try:
            fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            pass
        else:
            break
        strf = f"waiting 1s for {path}..."
        if pkg:
            pkg.log(strf)
        else:
            logger.get().out(f"cbuild: {strf}")
        time.sleep(1)
    try:
        yield fd
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def _archlock(rpath, arch):
    if not isinstance(arch, str):
        arch = arch.rparent.profile().arch
    return rpath / f"cbuild-{arch}.lock"


def apklock(arch):
    cpath = paths.cbuild_cache()
    # ensure it exists; this is needed because various operations
    # rely on apk locking even if the bldroot is not prepared, etc.
    if not cpath.is_dir():
        cpath.mkdir(parents=True, exist_ok=True)
    return cpath / f"apk-{arch}.lock"


def rootlock():
    return paths.bldroot() / ".lock"


def repolock(arch):
    return _archlock(paths.repository(), arch)


def stagelock(arch):
    return _archlock(paths.stage_repository(), arch)
