# Provides current locations of all the global paths.

import os

def init(distdir, masterdir, hostdir):
    global _ddir, _mdir, _hdir, _repo, _srcs, _srcps, _cbdir

    cwd = os.getcwd()
    _ddir = distdir
    _mdir = os.path.realpath(os.path.join(cwd, masterdir))
    _hdir = os.path.realpath(os.path.join(cwd, hostdir))

    _repo = os.path.join(_hdir, "binpkgs")
    _srcs = os.path.join(_hdir, "sources")
    _srcps = os.path.join(_ddir, "srcpkgs")

    _cbdir = os.path.join(_ddir, "cbuild")

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
