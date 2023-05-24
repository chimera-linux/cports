# Provides current locations of all the global paths.

import pathlib

_stage = 3


def init(cbuildir, distdir, rootdir, blddir, rdir, ardir, srdir, sdir, cdir):
    global _ddir, _bdir, _bldir, _rdir, _ardir, _srcs, _cbdir, _ccdir, _srdir

    cwd = pathlib.Path.cwd()
    _ddir = pathlib.Path(distdir)
    _bdir = (cwd / rootdir).resolve()
    if len(blddir) == 0:
        _bldir = None
    else:
        _bldir = (cwd / blddir).resolve()
    _rdir = (cwd / rdir).resolve()
    if ardir:
        _ardir = (cwd / ardir).resolve()
    else:
        _ardir = None
    _srcs = (cwd / sdir).resolve()
    _ccdir = (cwd / cdir).resolve()
    if srdir:
        _srdir = (cwd / srdir).resolve()
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
    _apkcmd = cmd


def apk():
    return _apkcmd


def distdir():
    return _ddir


def bldroot():
    return _bdir


def builddir():
    if not _bldir:
        return bldroot() / "builddir"
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


def cbuild_cache():
    return _ccdir


def cbuild():
    return _cbdir


def prepare():
    sources().mkdir(parents=True, exist_ok=True)
    (cbuild_cache() / "apk").mkdir(parents=True, exist_ok=True)
    repository().mkdir(parents=True, exist_ok=True)
    stage_repository().mkdir(parents=True, exist_ok=True)
    builddir().mkdir(parents=True, exist_ok=True)

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
