from cbuild.core import paths

from os import path
import re

def init():
    from cbuild import cpu

    global _install, _query, _reconf, _remove, _cvers, _rindex

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

def get_pkg_dep_name(s):
    found = re.search(r"[><\*\?\[\]]", s)
    if not found:
        return None

    sn = s[:found.start()]
    if sn.endswith("-"):
        sn = sn[0:len(sn) - 1]

    if len(sn) == 0:
        return None

    return sn

def _is_revision(s):
    if len(s) == 0:
        return False

    for i, c in enumerate(s):
        if not c.isdigit() and c != "_":
            return False

    return True

def get_pkg_name(s):
    idx = s.rfind("-")
    if idx <= 0:
        return None

    valid = False
    ps = s[idx + 1:]
    for i, c in enumerate(ps):
        if c == "_":
            break
        if c.isdigit():
            ridx = ps[i + 1:].find("_")
            if ridx >= 0:
                valid = _is_revision(ps[i + ridx + 2])
                break

    if not valid:
        return None

    return s[0:idx]

def get_pkg_version(s):
    idx = s.rfind("-")
    if idx <= 0:
        return None

    valid = False
    ps = s[idx + 1:]
    for i, c in enumerate(ps):
        if c == "_":
            break
        if c.isdigit():
            ridx = ps[i + 1:].find("_")
            if ridx >= 0:
                if _is_revision(ps[i + ridx + 2]):
                    return ps
                else:
                    return None

    return None
