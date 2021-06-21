from cbuild.core import paths, version
from cbuild import cpu

from os import path
import shlex
import subprocess
import pathlib
import fnmatch
import re

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

def _match_ver(pkgv, pattern):
    pass

_matchers = {
    "<": version.match,
    ">": version.match,
    "*": fnmatch.fnmatchcase,
    "?": fnmatch.fnmatchcase,
    "[": fnmatch.fnmatchcase,
    "]": fnmatch.fnmatchcase
}

def pkg_match(pkgv, pattern):
    if pkgv == pattern:
        return True

    global _matchers

    for c in pattern:
        f = _matchers.get(c, None)
        if f:
            return f(pkgv, pattern)

    return False
