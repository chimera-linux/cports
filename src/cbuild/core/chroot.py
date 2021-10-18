import subprocess
import os
import re
import glob
import shutil
import shlex
import getpass
import pathlib
from tempfile import mkstemp

from cbuild.core import logger, paths
from cbuild.apk import cli as apki

_chroot_checked = False
_chroot_ready = False

def host_cpu():
    return _host

def target_cpu():
    return _target

def set_target(tgt):
    global _target
    _target = tgt

def set_host(tgt):
    global _host
    _host = tgt

def chroot_check(force = False):
    global _chroot_checked, _chroot_ready

    if _chroot_checked and not force:
        return _chroot_ready

    _chroot_checked = True

    if (paths.bldroot() / ".cbuild_chroot_init").is_file():
        _chroot_ready = True
        cpun = (paths.bldroot() / ".cbuild_chroot_init").read_text().strip()
    else:
        _chroot_ready = False
        cpun = os.uname().machine

    set_host(cpun)
    set_target(cpun)

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

def _prepare_passwd():
    bfp = paths.distdir() / "main/base-files/files"
    tfp = paths.bldroot() / "etc"

    shutil.copy(bfp / "etc/passwd", tfp)
    shutil.copy(bfp / "etc/group", tfp)

    with open(tfp / "passwd", "a") as pf:
        pf.write(f"cbuild:x:1337:1337:cbuild user:/tmp:/bin/nologin\n")

    with open(tfp / "group", "a") as pf:
        pf.write(f"cbuild:x:1337:\n")

def _init():
    xdir = paths.bldroot() / "etc" / "apk"
    xdir.mkdir(parents = True, exist_ok = True)

    shutil.copy("/etc/resolv.conf", paths.bldroot() / "etc")

def _prepare(arch, stage):
    sfpath = paths.bldroot() / ".cbuild_chroot_init"
    if sfpath.is_file():
        return
    if not (paths.bldroot() / "usr" / "bin" / "sh").is_file():
        logger.get().out_red("cbuild: bootstrap not installed, can't continue")
        raise Exception()

    (paths.bldroot() / "etc" / "localtime").symlink_to(
        "../usr/share/zoneinfo/UTC"
    )

    _prepare_passwd()

    with open(sfpath, "w") as sf:
        sf.write(arch + "\n")

def setup_keys(rootp):
    # copy over apk public keys
    keydir = rootp / "etc/apk/keys"

    shutil.rmtree(keydir, ignore_errors = True)
    keydir.mkdir(parents = True, exist_ok = True)

    for f in (paths.distdir() / "etc/keys").glob("*.pub"):
        shutil.copy2(f, keydir)

_crepos = None

def get_confrepos():
    global _crepos

    if _crepos:
        return _crepos

    _crepos = []
    for f in (paths.distdir() / "etc/apk/repositories.d").glob("*.conf"):
        with open(f) as repof:
            for repo in repof:
                _crepos.append(repo.strip())

    return _crepos

def repo_sync(genrepos = False):
    setup_keys(paths.bldroot())

    # generate a repositories file for chroots
    rfile = paths.bldroot() / "etc/apk/repositories"
    # erase first in any case
    rfile.unlink(missing_ok = True)
    # generate only if needed (for explicit chroots)
    if genrepos:
        with rfile.open("w") as rfh:
            for rd in paths.repository().iterdir():
                for cr in get_confrepos():
                    cr = cr.lstrip("/")
                    idxp = rd / cr / host_cpu() / "APKINDEX.tar.gz"
                    if idxp.is_file():
                        rfh.write(f"/binpkgs/{rd.name}/{cr}\n")
            if paths.alt_repository():
                for rd in paths.alt_repository().iterdir():
                    for cr in get_confrepos():
                        cr = cr.lstrip("/")
                        idxp = rd / cr / host_cpu() / "APKINDEX.tar.gz"
                        if idxp.is_file():
                            rfh.write(f"/altbinpkgs/{rd.name}/{cr}\n")

    # do not refresh if chroot is not initialized
    if not (paths.bldroot() / ".cbuild_chroot_init").is_file():
        return

    if apki.call_chroot("update", [], "main").returncode != 0:
        logger.get().out_red(f"cbuild: failed to update pkg database")
        raise Exception()

def reconfigure():
    if not chroot_check():
        return

    statefile = paths.bldroot() / ".cbuild_chroot_configured"

    if statefile.is_file():
        return

    logger.get().out("cbuild: reconfiguring base...")

    if enter("update-ca-certificates", ["--fresh"]).returncode != 0:
        logger.get().out_red(f"cbuild: failed to reconfigure base")
        raise Exception()

    statefile.touch()

def initdb(path = None):
    # we init the database ourselves
    if not path:
        path = paths.bldroot()

    (path / "tmp").mkdir(parents = True, exist_ok = True)
    (path / "dev").mkdir(parents = True, exist_ok = True)
    (path / "etc/apk").mkdir(parents = True, exist_ok = True)
    (path / "usr/lib/apk/db").mkdir(parents = True, exist_ok = True)
    (path / "var/cache/apk").mkdir(parents = True, exist_ok = True)
    (path / "var/cache/misc").mkdir(parents = True, exist_ok = True)
    (path / "var/log").mkdir(parents = True, exist_ok = True)

    # largely because of custom usrmerge
    if not (path / "lib").is_symlink():
        (path / "lib").symlink_to("usr/lib")

    (path / "usr/lib/apk/db/installed").touch()
    (path / "etc/apk/world").touch()

def install(arch = None, stage = 2):
    if chroot_check():
        return

    logger.get().out("cbuild: installing base-chroot...")

    initdb()

    if not arch or stage < 2:
        arch = host_cpu()

    set_host(arch)
    set_target(arch)
    repo_sync()

    irun = apki.call(
        "add", ["--no-scripts", "base-chroot"], "main", arch = arch
    )
    if irun.returncode != 0:
        logger.get().out_red("cbuild: failed to install base-chroot")
        raise Exception()

    logger.get().out("cbuild: installed base-chroot successfully!")

    paths.prepare()
    _prepare(arch, stage)
    _chroot_checked = False
    _chroot_ready = False
    chroot_check()
    _init()

def remove_autodeps(bootstrapping):
    if bootstrapping is None:
        bootstrapping = not (paths.bldroot() / ".cbuild_chroot_init").is_file()

    log = logger.get()

    log.out("cbuild: removing autodeps...")

    failed = False

    if apki.call("info", [
        "--installed", "autodeps-host"
    ], None, capture_output = True, allow_untrusted = True).returncode == 0:
        if bootstrapping:
            del_ret = apki.call("del", [
                "--no-scripts", "autodeps-host"
            ], None, capture_output = True)
        else:
            del_ret = apki.call_chroot(
                "del", ["autodeps-host"], None, capture_out = True
            )

        if del_ret.returncode != 0:
            log.out_plain(">> stderr (host):")
            log.out_plain(del_ret.stderr.decode())
            failed = True

    if apki.call("info", [
        "--installed", "autodeps-target"
    ], None, capture_output = True, allow_untrusted = True).returncode == 0:
        if bootstrapping:
            del_ret = apki.call("del", [
                "--no-scripts", "autodeps-target"
            ], None, capture_output = True)
        else:
            del_ret = apki.call_chroot(
                "del", ["autodeps-target"], None, capture_out = True
            )

        if del_ret.returncode != 0:
            log.out_plain(">> stderr (target):")
            log.out_plain(del_ret.stderr.decode())
            failed = True

    if failed:
        log.out_red("cbuild: failed to remove autodeps")
        raise Exception()

def update(do_clean = True):
    if not chroot_check():
        return

    reconfigure()

    logger.get().out("cbuild: updating software in %s container..." \
        % str(paths.bldroot()))

    remove_autodeps(False)

    # reinit passwd/group
    _prepare_passwd()

    apki.call_chroot("update", ["-q"], "main", check = True)
    apki.call_chroot("upgrade", ["--available"], "main", check = True)

def enter(cmd, args = [], capture_out = False, check = False,
          env = {}, stdout = None, stderr = None, wrkdir = None,
          bootstrapping = False, ro_root = False, ro_build = False,
          ro_dest = True, unshare_all = False, mount_binpkgs = False,
          mount_ccache = False, pretend_uid = None, pretend_gid = None,
          new_session = True):
    defpath = "/usr/bin"
    if bootstrapping:
        defpath = "/usr/bin:" + os.environ["PATH"]

    envs = {
        "PATH": defpath,
        "SHELL": "/bin/sh",
        "HOME": "/tmp",
        "LC_COLLATE": "C",
        "LANG": "C.UTF-8",
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

    if new_session:
        envs["PYTHONUNBUFFERED"] = "1"

    # ccache path is searched first
    #
    # this has the implication of having ccache invoke whatever cc wrapper
    # we have at the time, rather than the other way around, which means
    # the wrappers don't have to account for ccache explicitly
    if "CCACHEPATH" in envs:
        envs["PATH"] = envs["CCACHEPATH"] + ":" + envs["PATH"]

    if ro_root:
        root_bind = "--ro-bind"
    else:
        root_bind = "--bind"

    if ro_build:
        build_bind = "--ro-bind"
    else:
        build_bind = "--bind"

    if ro_dest:
        dest_bind = "--ro-bind"
    else:
        dest_bind = "--bind"

    if bootstrapping:
        return subprocess.run(
            [cmd] + args, env = envs,
            capture_output = capture_out, check = check,
            stdout = stdout, stderr = stderr,
            cwd = os.path.abspath(wrkdir) if wrkdir else None
        )

    bcmd = [
        "bwrap",
        root_bind, paths.bldroot(), "/",
        build_bind, paths.bldroot() / "builddir", "/builddir",
        dest_bind, paths.bldroot() / "destdir", "/destdir",
        "--ro-bind", paths.sources(), "/sources",
        "--dev", "/dev",
        "--proc", "/proc",
        "--tmpfs", "/tmp",
    ]

    if new_session:
        bcmd += ["--new-session", "--die-with-parent"]

    if mount_binpkgs:
        bcmd += ["--ro-bind", paths.repository(), "/binpkgs"]
        if paths.alt_repository():
            bcmd += ["--ro-bind", paths.alt_repository(), "/altbinpkgs"]

    if mount_ccache:
        bcmd += ["--bind", paths.ccache(), "/ccache"]

    if pretend_uid is None:
        pretend_uid = 1337
    if pretend_gid is None:
        pretend_gid = 1337

    bcmd += ["--uid", str(pretend_uid)]
    bcmd += ["--gid", str(pretend_gid)]

    if unshare_all:
        bcmd += ["--unshare-all"]

    if wrkdir:
        bcmd.append("--chdir")
        bcmd.append(wrkdir)

    bcmd.append(cmd)
    bcmd += args

    return subprocess.run(
        bcmd, env = envs, capture_output = capture_out, check = check,
        stdout = stdout, stderr = stderr
    )
