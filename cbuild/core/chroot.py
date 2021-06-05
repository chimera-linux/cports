import subprocess
import os
import re
import glob
import shutil
import shlex
import getpass
from os import path
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

    if os.path.isfile(os.path.join(paths.masterdir(), ".xbps_chroot_init")):
        _chroot_ready = True
        with open(os.path.join(paths.masterdir(), ".xbps_chroot_init")) as f:
            cpun = f.read().strip()
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
    xdir = path.join(paths.masterdir(), "etc", "xbps")
    os.makedirs(xdir, exist_ok = True)

    shf = open(path.join(paths.masterdir(), "bin", "xbps-shell"), "w")
    shf.write(f"""#!/bin/sh

PATH=/void-packages:/usr/bin

exec env -i -- SHELL=/bin/sh PATH="$PATH" \
    XBPS_ARCH={cpu.host()} XBPS_CHECK_PKGS="" \
    IN_CHROOT=1 LC_COLLATE=C LANG=en_US.UTF-8 TERM=linux HOME="/tmp" \
    PS1="[\\u@{paths.masterdir()} \\W]$ " /bin/bash +h
""")
    shf.close()

    dof = open(path.join(paths.masterdir(), "bin", "cbuild-do"), "w")
    dof.write("""#!/bin/sh
[ -n "$XBPS_STATEDIR" ] && export PATH="${XBPS_STATEDIR}/wrappers:$PATH"
cd $1
shift
exec "$@"
""")
    dof.close()

    os.chmod(path.join(paths.masterdir(), "bin", "xbps-shell"), 0o755)
    os.chmod(path.join(paths.masterdir(), "bin", "cbuild-do"), 0o755)

    shutil.copy("/etc/resolv.conf", path.join(paths.masterdir(), "etc"))

def _prepare(arch = None):
    sfpath = path.join(paths.masterdir(), ".xbps_chroot_init")
    if path.isfile(sfpath):
        return
    if not path.isfile(path.join(paths.masterdir(), "bin", "bash")):
        logger.get().out_red("cbuild: bootstrap not installed, can't continue")
        raise Exception()

    if path.isfile("/usr/share/zoneinfo/UTC"):
        zpath = path.join(paths.masterdir(), "usr", "share", "zoneinfo")
        os.makedirs(zpath, exist_ok = True)
        shutil.copy("/usr/share/zoneinfo/UTC", zpath)
        os.symlink("../usr/share/zoneinfo/UTC", path.join(
            paths.masterdir(), "etc", "localtime"
        ))
    else:
        logger.get().out(
            "cbuild: no local timezone configuration file created"
        )

    for f in ["dev", "sys", "tmp", "proc", "host", "boot", "void-packages"]:
        os.makedirs(path.join(paths.masterdir(), f), exist_ok = True)

    shutil.copy(
        path.join(paths.masterdir(), "base-files", "files", "passwd"),
        path.join(paths.masterdir(), "etc")
    )
    shutil.copy(
        path.join(paths.masterdir(), "base-files", "files", "group"),
        path.join(paths.masterdir(), "etc")
    )
    shutil.copy(
        path.join(paths.masterdir(), "base-files", "files", "hosts"),
        path.join(paths.masterdir(), "etc")
    )

    pf = open(path.join(paths.masterdir(), "etc", "passwd"), "a")
    username = getpass.getuser()
    gid = os.getgid()
    uid = os.getuid()
    pf.write(f"{username}:x:{uid}:{gid}:{username} user:/tmp:/bin/xbps-shell\n")
    pf.close()

    pf = open(path.join(paths.masterdir(), "etc", "group"), "a")
    pf.write(f"{username}:x:{gid}:\n")
    pf.close()

    sf = open(sfpath, "w")
    sf.write(arch + "\n")
    sf.close()

def repo_sync():
    confdir = path.join(paths.masterdir(), "etc", "xbps.d")

    if path.isdir(confdir):
        shutil.rmtree(confdir, onerror = _remove_ro)

    os.makedirs(confdir, exist_ok = True)
    try:
        os.remove(path.join(confdir, "00-repository-alt-local.conf"))
    except:
        pass

    # disable main repository conf
    os.symlink("/dev/null", path.join(confdir, "00-repository-main.conf"))

    # generate xbps.d(5) config files for repos
    _subst_in("/host", paths.hostdir(), path.join(
        paths.distdir(), "etc", "xbps.d", "repos-local.conf"
    ), path.join(confdir, "10-repository-local.conf"))

    rmlist = glob.glob(path.join(confdir, "*remote*"))
    for f in rmlist:
        try:
            os.remove(f)
        except:
            pass

    apf = open(path.join(confdir, "00-xbps-src.conf"), "a")
    apf.write("\nsyslog=false\n")
    apf.close()

def reconfigure():
    if not chroot_check():
        return

    statefile = path.join(paths.masterdir(), ".xbps_chroot_configured")

    if path.isfile(statefile):
        return

    logger.get().out("cbuild: reconfiguring base-chroot...")

    pkgs = [ "ca-certificates" ]
    for pkg in pkgs:
        if invoke_query([pkg]):
            invoke_reconfigure(["-f", pkg])

    f = open(statefile, "w")
    f.close()

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

    if invoke_xcmd(
        xbps.install(), ["-y", "base-chroot"],
        env = cenv, capture_out = False
    ).returncode != 0:
        logger.get().out_red("cbuild: failed to install base-chroot")
        raise Exception()

    if invoke_query(["base-files"]):
        invoke_reconfigure(["-f", "base-files"], env = {"XBPS_ARCH": arch})

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
        % paths.masterdir())

def enter(cmd, args = [], set_env = True, capture_out = False, check = False,
          env = {}, stdout = None, stderr = None):
    if not set_env:
        if bool(env):
            envs = dict(os.environ).update(env)
        else:
            envs = None
    else:
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
    return subprocess.run(
        [
            "bwrap",
            "--dev-bind", paths.masterdir(), "/",
            "--dev-bind", paths.hostdir(), "/host",
            "--dev-bind", paths.distdir(), "/void-packages",
            "--dev", "/dev",
            "--proc", "/proc",
            "--tmpfs", "/tmp",
            cmd
        ] + args,
        env = envs, capture_output = capture_out, check = check,
        stdout = stdout, stderr = stderr
    )

def invoke_xcmd(
    cmd, args, capture_out = True, check = False, env = {}, chroot = False,
    yes_input = False
):
    qs = shlex.split(cmd)
    if not chroot_check() or not chroot:
        return subprocess.run(
            qs + args,
            env = dict(os.environ).update(env) if bool(env) else None,
            capture_output = capture_out, check = check
        )
    return enter(
        qs[0], qs[1:] + args, capture_out = capture_out, check = check,
        env = env, input = "yes\n".encode() if yes_input else None
    )

def invoke_query(args, capture_out = True, yes_input = False):
    return invoke_xcmd(
        xbps.query(), args, capture_out = capture_out,
        yes_input = yes_input
    )

def invoke_reconfigure(
    args, capture_out = False, check = True, env = {}, yes_input = False
):
    return invoke_xcmd(
        xbps.reconfigure(), args, capture_out = capture_out,
        check = check, env = env, yes_input = yes_input
    )
