from cbuild.core import paths
from cbuild import cpu

from os import path
import shlex
import subprocess
import os
import re

def repository_url(pkgn):
    v = subprocess.run(
        [
            "xbps-query",
            "-c", path.join(paths.hostdir(), "repocache-" + cpu.host()),
            "-r", paths.masterdir(), "-C", "etc/xbps.d",
            "-R", "-prepository", pkgn
        ],
        capture_output = True
    ).stdout.strip().decode("ascii")

    if len(v) == 0:
        return None

    return v

def reconfigure(pkgn = None, arch = None, capture_out = False):
    rcenv = {"XBPS_ARCH": arch if arch else cpu.host()}

    if not pkgn:
        v = subprocess.run(
            ["xbps-reconfigure", "-r", paths.masterdir(), "-a"],
            capture_output = capture_out, env = rcenv
        )
        if not capture_out:
            return v.returncode == 0
        return v.returncode == 0, v.stdout, v.stderr

    if subprocess.run([
        "xbps-query", "-r", paths.masterdir(), "-C", pkgn
    ], capture_output = True).returncode != 0:
        if not capture_out:
            return True
        return True, None, None

    v = subprocess.run(
        ["xbps-reconfigure", "-r", paths.masterdir(), "-f", pkgn],
        env = rcenv, capture_output = capture_out
    )
    if not capture_out:
        return v.returncode == 0
    return v.returncode == 0, v.stdout, v.stderr

def install(pkglist, arch = None, capture_out = False):
    if arch:
        cenv = {"XBPS_TARGET_ARCH": arch}
    else:
        cenv = {}

    v = subprocess.run(
        [
            "xbps-install",
            "-c", path.join(paths.hostdir(), "repocache-" + cpu.host()),
            "-r", paths.masterdir(), "-C", "etc/xbps.d", "-Ay"
        ] + pkglist, env = cenv, capture_output = capture_out
    )
    if not capture_out:
        return v.returncode == 0
    return v.returncode == 0, v.stdout, v.stderr

def remove_orphans():
    v = subprocess.run(
        ["xbps-remove", "-r", paths.masterdir(), "-Ryod"],
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
            ["xbps-remove", "-r", paths.masterdir(), "-Ryod"],
            input = b"yes", capture_output = True
        )

    return v.returncode == 0, sout, serr

def checkvers(tmpls):
    out = subprocess.run(
        [
            "xbps-checkvers", "-r", paths.masterdir(),
            "-D", paths.distdir(), "-sm"
        ] + tmpls,
        capture_output = True
    ).stdout.strip().decode("ascii")

    ret = []
    for ln in out.split("\n"):
        if len(ln) == 0:
            continue
        ret.append(tuple(ln.split()[0:5]))

    return ret

def register_pkgs(pkglist, repopath, force = False):
    if not os.path.isdir(repopath):
        return False
    # subshell so we cd safely
    cmd = f"cd {shlex.quote(repopath)} && xbps-rindex "
    if force:
        cmd += "-f "
    cmd += "-a "
    cmd += " ".join(pkglist)
    return subprocess.run(cmd, shell = True)

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
