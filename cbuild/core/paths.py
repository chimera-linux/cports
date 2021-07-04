# Provides current locations of all the global paths.

import pathlib

_stage = 2

def init(distdir, masterdir, hostdir):
    global _ddir, _mdir, _hdir, _srcs, _srcps, _cbdir

    cwd = pathlib.Path.cwd()
    _ddir = pathlib.Path(distdir)
    _mdir = (cwd / masterdir).resolve()
    _hdir = (cwd / hostdir).resolve()

    _srcs = _hdir / "sources"
    _srcps = _ddir / "srcpkgs"

    _cbdir = _ddir / "cbuild"

def reinit_masterdir(masterdir, stage):
    global _mdir
    if stage == 2:
        _mdir = masterdir
    else:
        oname = masterdir.name
        _mdir = masterdir.with_name(oname + "-stage" + str(stage))

def set_stage(stage):
    global _stage
    _stage = stage

def distdir():
    return _ddir

def masterdir():
    return _mdir

def hostdir():
    return _hdir

def repository():
    if _stage == 2:
        return hostdir() / "binpkgs"
    else:
        return hostdir() / ("binpkgs-stage" + str(_stage))

def sources():
    return _srcs

def templates():
    return _srcps

def cbuild():
    return _cbdir

def prepare():
    hostdir().mkdir(parents = True, exist_ok = True)
    sources().mkdir(parents = True, exist_ok = True)
    masterdir().mkdir(parents = True, exist_ok = True)
    repository().mkdir(parents = True, exist_ok = True)
