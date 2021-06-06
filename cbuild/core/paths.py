# Provides current locations of all the global paths.

import pathlib

def init(distdir, masterdir, hostdir):
    global _ddir, _mdir, _hdir, _repo, _srcs, _srcps, _cbdir

    cwd = pathlib.Path.cwd()
    _ddir = pathlib.Path(distdir)
    _mdir = (cwd / masterdir).resolve()
    _hdir = (cwd / hostdir).resolve()

    _repo = _hdir / "binpkgs"
    _srcs = _hdir / "sources"
    _srcps = _ddir / "srcpkgs"

    _cbdir = _ddir / "cbuild"

def distdir():
    return _ddir

def masterdir():
    return _mdir

def hostdir():
    return _hdir

def repository():
    return _repo

def sources():
    return _srcs

def templates():
    return _srcps

def cbuild():
    return _cbdir
