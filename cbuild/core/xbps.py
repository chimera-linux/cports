from cbuild.core import paths

from os import path

def init():
    from cbuild import cpu

    global _uhelper, _install, _query, _reconf, _remove, _cvers, _rindex

    _uhelper = "xbps-uhelper -r " + paths.masterdir()
    _install = "xbps-install -c " + \
        path.join(paths.hostdir(), "repocache-" + cpu.host()) + \
        " -r " + paths.masterdir() + " -C etc/xbps.d"
    _query = "xbps-query -c " + \
        path.join(paths.hostdir(), "repocache-" + cpu.host()) + \
        " -r " + paths.masterdir() + " -C etc/xbps.d"
    _reconf = "xbps-reconfigure -r " + paths.masterdir()
    _remove = "xbps-remove -r " + paths.masterdir()
    _cvers = "xbps-checkvers -r " + paths.masterdir()
    _rindex = "xbps-rindex"

def uhelper():
    return _uhelper

def install():
    return _install

def query():
    return _query

def reconfigure():
    return _reconf

def remove():
    return _remove

def checkvers():
    return _cvers

def rindex():
    return _rindex
