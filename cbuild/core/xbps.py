from cbuild.core import paths, version
from cbuild import cpu

from os import path
import shlex
import subprocess
import pathlib
import fnmatch
import re

def repository_properties(pkgn, plist):
    v = subprocess.run(
        [
            "xbps-query",
            "-c", str(paths.hostdir() / ("repocache-" + cpu.host())),
            "-r", str(paths.masterdir()), "-C", "etc/xbps.d",
            "-R", "-p" + ",".join(plist), pkgn
        ],
        capture_output = True
    ).stdout.strip().decode("ascii")

    if len(v) == 0:
        return None

    if len(plist) == 1:
        return v

    return v.split("\n")

def repository_url(pkgn):
    return repository_properties(pkgn, ["repository"])

def reconfigure(pkgn = None, arch = None, capture_out = False):
    rcenv = {"XBPS_ARCH": arch if arch else cpu.host()}

    if not pkgn:
        v = subprocess.run(
            ["xbps-reconfigure", "-r", str(paths.masterdir()), "-a"],
            capture_output = capture_out, env = rcenv
        )
        if not capture_out:
            return v.returncode == 0
        return v.returncode == 0, v.stdout, v.stderr

    if subprocess.run([
        "xbps-query", "-r", str(paths.masterdir()), "-C", pkgn
    ], capture_output = True).returncode != 0:
        if not capture_out:
            return True
        return True, None, None

    v = subprocess.run(
        ["xbps-reconfigure", "-r", str(paths.masterdir()), "-f", pkgn],
        env = rcenv, capture_output = capture_out
    )
    if not capture_out:
        return v.returncode == 0
    return v.returncode == 0, v.stdout, v.stderr

def install(pkglist, arch = None, capture_out = False, automatic = True):
    if arch:
        cenv = {"XBPS_TARGET_ARCH": arch}
    else:
        cenv = {}

    v = subprocess.run(
        [
            "xbps-install",
            "-c", str(paths.hostdir() / ("repocache-" + cpu.host())),
            "-r", str(paths.masterdir()), "-C", "etc/xbps.d",
            "-Ay" if automatic else "-y"
        ] + pkglist, env = cenv, capture_output = capture_out
    )
    if not capture_out:
        return v.returncode == 0
    return v.returncode == 0, v.stdout, v.stderr

def remove_orphans():
    v = subprocess.run(
        ["xbps-remove", "-r", str(paths.masterdir()), "-Ryod"],
        input = b"yes", capture_output = True
    )
    sout = b""
    serr = b""

    while v.returncode == 0:
        if len(v.stdout.strip()) == 0:
            break
        sout += v.stdout
        serr += v.stderr
        v = subprocess.run(
            ["xbps-remove", "-r", str(paths.masterdir()), "-Ryod"],
            input = b"yes", capture_output = True
        )

    return v.returncode == 0, sout, serr

def register_pkgs(pkglist, repopath, force = False):
    if not pathlib.Path(repopath).is_dir():
        return False
    # subshell so we cd safely
    cmd = f"cd {shlex.quote(str(repopath))} && xbps-rindex "
    if force:
        cmd += "-f "
    cmd += "-a "
    cmd += " ".join(pkglist)
    return subprocess.run(cmd, shell = True).returncode == 0

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

def get_installed_version(pkg):
    out = subprocess.run(
        [
            "xbps-uhelper", "-r", str(paths.masterdir()),
            "version", pkg
        ],
        capture_output = True, env = {"XBPS_ARCH": cpu.host()}
    ).stdout.strip().decode("ascii")

    if len(out) == 0:
        return None

    return out

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
