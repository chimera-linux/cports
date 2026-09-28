# Provides current locations of all the global paths.

import pathlib
import os.path

_stage = 3


def _expath(cwd, path):
    return (cwd / os.path.expanduser(path)).resolve()


def init(cbuildir, distdir, rootdir, blddir, rdir, ardir, srdir, sdir, cdir):
    global _ddir, _bdir, _bldir, _rdir, _ardir, _srcs, _cbdir, _ccdir, _srdir

    cwd = pathlib.Path.cwd()
    _ddir = pathlib.Path(distdir)
    _bdir = _expath(cwd, rootdir)
    if len(blddir) == 0:
        _bldir = None
    else:
        _bldir = _expath(cwd, blddir)
    _rdir = _expath(cwd, rdir)
    if ardir:
        _ardir = _expath(cwd, ardir)
    else:
        _ardir = None
    _srcs = _expath(cwd, sdir)
    _ccdir = _expath(cwd, cdir)
    if srdir:
        _srdir = _expath(cwd, srdir)
    else:
        _srdir = None

    _cbdir = pathlib.Path(cbuildir) / "cbuild"


def reinit_buildroot(rootdir, stage):
    global _bdir
    if stage == 3:
        _bdir = rootdir
    else:
        oname = rootdir.name
        _bdir = rootdir.with_name(f"{oname}-stage{stage}")


def set_stage(stage):
    global _stage
    _stage = stage


def set_apk(cmd):
    global _apkcmd
    _apkcmd = os.path.expanduser(cmd)


def apk():
    # for stage 0 we always use host apk
    # for stage 1 we still use host apk as stage0 does not build static
    if _stage > 1:
        sapk = bldroot() / "usr/bin/apk.static"
        if sapk.is_file():
            return sapk
    # fall back to host apk if no bldroot and so on
    return _apkcmd


def set_bwrap(cmd):
    global _bwcmd
    _bwcmd = os.path.expanduser(cmd)


def bwrap():
    return _bwcmd


def distdir():
    return _ddir


def bldroot():
    return _bdir


def builddir():
    if not _bldir:
        return bldroot()
    else:
        return _bldir


def alt_repository():
    return _ardir


def repository():
    if _stage == 3:
        return _rdir
    else:
        return _rdir.with_name(f"{_rdir.name}-stage{_stage}")


def stage_repository():
    if _stage == 3:
        return _srdir
    else:
        return _srdir.with_name(f"{_srdir.name}-stage{_stage}")


def sources():
    return _srcs


def init_keys(kp):
    global _keys
    _keys = _expath(pathlib.Path.cwd(), kp)


def keys():
    return _keys


def cbuild_cache():
    return _ccdir


def cbuild():
    return _cbdir


def prepare():
    sources().mkdir(parents=True, exist_ok=True)
    (cbuild_cache() / "apk").mkdir(parents=True, exist_ok=True)
    repository().mkdir(parents=True, exist_ok=True)
    stage_repository().mkdir(parents=True, exist_ok=True)
    (builddir() / "builddir").mkdir(parents=True, exist_ok=True)
    (builddir() / "destdir").mkdir(parents=True, exist_ok=True)

    # prepare build root
    for f in [
        "builddir",
        "destdir",
        "binpkgs",
        "altbinpkgs",
        "stagepkgs",
        "sources",
        "cbuild_cache",
        "dev",
        "sys",
        "tmp",
        "proc",
        "host",
        "boot",
    ]:
        (bldroot() / f).mkdir(parents=True, exist_ok=True)
