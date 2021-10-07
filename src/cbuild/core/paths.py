# Provides current locations of all the global paths.

import pathlib

_stage = 2

def init(cbuildir, distdir, rootdir, rdir, ardir, sdir, cdir):
    global _ddir, _bdir, _rdir, _ardir, _srcs, _cbdir, _ccdir

    cwd = pathlib.Path.cwd()
    _ddir = pathlib.Path(distdir)
    _bdir = (cwd / rootdir).resolve()
    _rdir = (cwd / rdir).resolve()
    if ardir:
        _ardir = (cwd / ardir).resolve()
    else:
        _ardir = None
    _srcs = (cwd / sdir).resolve()
    _ccdir = (cwd / cdir).resolve()

    _cbdir = pathlib.Path(cbuildir) / "cbuild"

def reinit_buildroot(rootdir, stage):
    global _bdir
    if stage == 2:
        _bdir = rootdir
    else:
        oname = rootdir.name
        _bdir = rootdir.with_name(f"{oname}-stage{stage}")

def set_stage(stage):
    global _stage
    _stage = stage

def distdir():
    return _ddir

def bldroot():
    return _bdir

def alt_repository():
    return _ardir

def repository():
    if _stage == 2:
        return _rdir
    else:
        return _rdir.with_name(f"{_rdir.name}-stage{_stage}")

def sources():
    return _srcs

def ccache():
    return _ccdir

def cbuild():
    return _cbdir

def prepare():
    sources().mkdir(parents = True, exist_ok = True)
    ccache().mkdir(parents = True, exist_ok = True)
    (bldroot() / "builddir").mkdir(parents = True, exist_ok = True)
    (bldroot() / "destdir").mkdir(parents = True, exist_ok = True)
    repository().mkdir(parents = True, exist_ok = True)

    # prepare build root
    for f in [
        "builddir", "destdir", "binpkgs", "altbinpkgs", "sources", "ccache",
        "dev", "sys", "tmp", "proc", "host", "boot",
    ]:
        (bldroot() / f).mkdir(parents = True, exist_ok = True)
