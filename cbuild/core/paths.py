# Provides current locations of all the global paths.

import pathlib

_stage = 2

def init(distdir, rootdir, hostdir):
    global _ddir, _bdir, _hdir, _srcs, _cbdir

    cwd = pathlib.Path.cwd()
    _ddir = pathlib.Path(distdir)
    _bdir = (cwd / rootdir).resolve()
    _hdir = (cwd / hostdir).resolve()

    _srcs = _hdir / "sources"
    _cbdir = _ddir / "cbuild"

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

def hostdir():
    return _hdir

def repository():
    if _stage == 2:
        return hostdir() / "binpkgs"
    else:
        return hostdir() / f"binpkgs-stage{_stage}"

def sources():
    return _srcs

def cbuild():
    return _cbdir

def prepare():
    hostdir().mkdir(parents = True, exist_ok = True)
    sources().mkdir(parents = True, exist_ok = True)
    (bldroot() / "builddir").mkdir(parents = True, exist_ok = True)
    (bldroot() / "destdir").mkdir(parents = True, exist_ok = True)
    repository().mkdir(parents = True, exist_ok = True)
    (hostdir() / "ccache").mkdir(exist_ok = True)

    # prepare build root
    for f in [
        "builddir", "destdir", "binpkgs", "sources", "ccache",
        "dev", "sys", "tmp", "proc", "host", "boot",
    ]:
        (bldroot() / f).mkdir(parents = True, exist_ok = True)
