import subprocess
import os
import re
import glob
import shutil
import shlex
import getpass
import pathlib
from tempfile import mkstemp

from cbuild.core import logger, paths, xbps
from cbuild import cpu

_chroot_checked = False
_chroot_ready = False

def chroot_check():
    global _chroot_checked, _chroot_ready

    if _chroot_checked:
        return _chroot_ready

    _chroot_checked = True

    if (paths.masterdir() / ".xbps_chroot_init").is_file():
        _chroot_ready = True
        cpun = (paths.masterdir() / ".xbps_chroot_init").read_text().strip()
        cpu.init(cpun, cpun)
    else:
        cpun = os.uname().machine + "-musl"
        cpu.init(cpun, cpun)

    return _chroot_ready

def _subst_in(pat, rep, src, dest = None):
    inf = open(src, "r")
    if dest:
        outf = open(dest, "w")
    else:
        fd, nm = mkstemp()
        outf = open(nm, "w")

    for line in inf:
        out = re.sub(pat, rep, line)
        outf.write(out)

    inf.close()
    outf.close()

    if not dest:
        shutil.move(nm, src)

def _remove_ro(f, path, _):
    os.chmod(path, stat.S_IWRITE)
    f(path)

def _init():
    xdir = paths.masterdir() / "etc" / "xbps"
    os.makedirs(xdir, exist_ok = True)

    shf = open(paths.masterdir() / "bin" / "xbps-shell", "w")
    shf.write(f"""#!/bin/sh

PATH=/void-packages:/usr/bin

exec env -i -- SHELL=/bin/sh PATH="$PATH" \
    XBPS_ARCH={cpu.host()} XBPS_CHECK_PKGS="" \
    IN_CHROOT=1 LC_COLLATE=C LANG=en_US.UTF-8 TERM=linux HOME="/tmp" \
    PS1="[\\u@{str(paths.masterdir())} \\W]$ " /bin/bash +h
""")
    shf.close()

    (paths.masterdir() / "bin" / "xbps-shell").chmod(0o755)

    shutil.copy("/etc/resolv.conf", paths.masterdir() / "etc")

def _prepare(arch = None):
    sfpath = paths.masterdir() / ".xbps_chroot_init"
    if sfpath.is_file():
        return
    if not (paths.masterdir() / "usr" /"bin" / "bash").is_file():
        logger.get().out_red("cbuild: bootstrap not installed, can't continue")
        raise Exception()

    if pathlib.Path("/usr/share/zoneinfo/UTC").is_file():
        zpath = paths.masterdir() / "usr" / "share" / "zoneinfo"
        os.makedirs(zpath, exist_ok = True)
        shutil.copy("/usr/share/zoneinfo/UTC", zpath)
        (paths.masterdir() / "etc" / "localtime").symlink_to(
            "../usr/share/zoneinfo/UTC"
        )
    else:
        logger.get().out(
            "cbuild: no local timezone configuration file created"
        )

    for f in ["dev", "sys", "tmp", "proc", "host", "boot", "void-packages"]:
        os.makedirs(paths.masterdir() / f, exist_ok = True)

    shutil.copy(
        paths.templates() / "base-files" / "files" / "passwd",
        paths.masterdir() / "etc"
    )
    shutil.copy(
        paths.templates() / "base-files" / "files" / "group",
        paths.masterdir() / "etc"
    )
    shutil.copy(
        paths.templates() / "base-files" / "files" / "hosts",
        paths.masterdir() / "etc"
    )

    with open(paths.masterdir() / "etc" / "passwd", "a") as pf:
        username = getpass.getuser()
        gid = os.getgid()
        uid = os.getuid()
        pf.write(f"{username}:x:{uid}:{gid}:{username} user:/tmp:/bin/xbps-shell\n")

    with open(paths.masterdir() / "etc" / "group", "a") as pf:
        pf.write(f"{username}:x:{gid}:\n")

    with open(sfpath, "w") as sf:
        sf.write(arch + "\n")

def repo_sync():
    confdir = paths.masterdir() / "etc" / "xbps.d"

    if confdir.is_dir():
        shutil.rmtree(confdir, onerror = _remove_ro)

    os.makedirs(confdir, exist_ok = True)
    (confdir / "00-repository-alt-local.conf").unlink(missing_ok = True)

    # disable main repository conf
    (confdir / "00-repository-main.conf").symlink_to("/dev/null")

    # generate xbps.d(5) config files for repos
    _subst_in("/host", str(paths.hostdir()), str(
        paths.distdir() / "etc" / "xbps.d" / "repos-local.conf"
    ), str(confdir / "10-repository-local.conf"))

    rmlist = confdir.glob("*remote*")
    for f in rmlist:
        f.unlink(missing_ok = True)

    with open(confdir / "00-xbps-src.conf", "a") as apf:
        apf.write("\nsyslog=false\n")

def reconfigure():
    if not chroot_check():
        return

    statefile = paths.masterdir() / ".xbps_chroot_configured"

    if statefile.is_file():
        return

    logger.get().out("cbuild: reconfiguring base-chroot...")

    pkgs = [ "ca-certificates" ]
    for pkg in pkgs:
        if not xbps.reconfigure(pkg):
            logger.get().out_red(f"cbuild: failed to reconfigure {pkg}")
            raise Exception()

    statefile.touch()

def install(arch = None, bootstrap = False):
    if chroot_check():
        return

    logger.get().out("cbuild: installing base-chroot...")

    oldh = cpu.host()
    oldt = cpu.target()
    try:
        cpu.init(arch, oldt)
        repo_sync()
    finally:
        cpu.init(oldh, oldt)

    cenv = {}
    if not bootstrap:
        cenv["XBPS_TARGET_ARCH"] = arch

    if not xbps.install(
        ["base-chroot"], arch = arch if not bootstrap else None
    ):
        logger.get().out_red("cbuild: failed to install base-chroot")
        raise Exception()

    if not xbps.reconfigure("base-files", arch = arch):
        logger.get().out_red("cbuild: failed to configure chroot")
        raise Exception()

    logger.get().out("cbuild: installed base-chroot successfully!")

    _prepare(arch)
    _chroot_checked = False
    _chroot_ready = False
    chroot_check()
    _init()

def update(do_clean = True):
    if not chroot_check():
        return

    reconfigure()

    logger.get().out("cbuild: updating software in %s masterdir..." \
        % str(paths.masterdir()))

def enter(cmd, args = [], capture_out = False, check = False,
          env = {}, stdout = None, stderr = None, wrkdir = None,
          bootstrapping = False):
    envs = {
        "PATH": "/usr/bin:" + os.environ["PATH"],
        "SHELL": "/bin/sh",
        "HOME": "/tmp",
        "IN_CHROOT": "1",
        "LC_COLLATE": "C",
        "LANG": "en_US.UTF-8",
        **env
    }
    if "NO_PROXY" in os.environ:
        envs["NO_PROXY"] = os.environ["NO_PROXY"]
    if "FTP_PROXY" in os.environ:
        envs["FTP_PROXY"] = os.environ["FTP_PROXY"]
    if "HTTP_PROXY" in os.environ:
        envs["HTTP_PROXY"] = os.environ["HTTP_PROXY"]
    if "HTTPS_PROXY" in os.environ:
        envs["HTTPS_PROXY"] = os.environ["HTTPS_PROXY"]
    if "SOCKS_PROXY" in os.environ:
        envs["SOCKS_PROXY"] = os.environ["SOCKS_PROXY"]
    if "FTP_RETRIES" in os.environ:
        envs["FTP_RETRIES"] = os.environ["FTP_RETRIES"]
    if "HTTP_PROXY_AUTH" in os.environ:
        envs["HTTP_PROXY_AUTH"] = os.environ["HTTP_PROXY_AUTH"]

    # if running from template, ensure wrappers are early in executable path
    if "CBUILD_STATEDIR" in envs:
        envs["PATH"] = envs["CBUILD_STATEDIR"] + "/wrappers:" + envs["PATH"]

    if bootstrapping:
        return subprocess.run(
            [cmd] + args, env = envs,
            capture_output = capture_out, check = check,
            stdout = stdout, stderr = stderr,
            cwd = os.path.abspath(wrkdir) if wrkdir else None
        )

    bcmd = [
        "bwrap",
        "--dev-bind", str(paths.masterdir()), "/",
        "--dev-bind", str(paths.hostdir()), "/host",
        "--dev-bind", str(paths.distdir()), "/void-packages",
        "--dev", "/dev",
        "--proc", "/proc",
        "--tmpfs", "/tmp",
    ]

    if wrkdir:
        bcmd.append("--chdir")
        bcmd.append(str(wrkdir))

    bcmd.append(cmd)
    bcmd += args

    return subprocess.run(
        bcmd, env = envs, capture_output = capture_out, check = check,
        stdout = stdout, stderr = stderr
    )
