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

    if (paths.masterdir() / ".cbuild_chroot_init").is_file():
        _chroot_ready = True
        cpun = (paths.masterdir() / ".cbuild_chroot_init").read_text().strip()
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

def _init():
    xdir = paths.masterdir() / "etc" / "apk"
    xdir.mkdir(parents = True, exist_ok = True)

    shf = open(paths.masterdir() / "bin" / "cbuild-shell", "w")
    shf.write(f"""#!/bin/sh

PATH=/usr/bin

exec env -i -- SHELL=/bin/sh PATH="$PATH" \
    CBUILD_ARCH={host_cpu()} \
    IN_CHROOT=1 LC_COLLATE=C LANG=en_US.UTF-8 TERM=linux HOME="/tmp" \
    PS1='$PWD$ ' /bin/sh
""")
    shf.close()

    (paths.masterdir() / "bin" / "cbuild-shell").chmod(0o755)

    shutil.copy("/etc/resolv.conf", paths.masterdir() / "etc")

def _prepare(arch, stage):
    sfpath = paths.masterdir() / ".cbuild_chroot_init"
    if sfpath.is_file():
        return
    if not (paths.masterdir() / "usr" / "bin" / "sh").is_file():
        logger.get().out_red("cbuild: bootstrap not installed, can't continue")
        raise Exception()

    if pathlib.Path("/usr/share/zoneinfo/UTC").is_file():
        zpath = paths.masterdir() / "usr" / "share" / "zoneinfo"
        zpath.mkdir(parents = True, exist_ok = True)
        shutil.copy("/usr/share/zoneinfo/UTC", zpath)
        (paths.masterdir() / "etc" / "localtime").symlink_to(
            "../usr/share/zoneinfo/UTC"
        )
    else:
        logger.get().out(
            "cbuild: no local timezone configuration file created"
        )

    with open(paths.masterdir() / "etc" / "passwd", "a") as pf:
        username = getpass.getuser()
        gid = os.getgid()
        uid = os.getuid()
        pf.write(f"{username}:x:{uid}:{gid}:{username} user:/tmp:/bin/cbuild-shell\n")

    with open(paths.masterdir() / "etc" / "group", "a") as pf:
        pf.write(f"{username}:x:{gid}:\n")

    with open(sfpath, "w") as sf:
        sf.write(arch + "\n")

def setup_keys(rootp):
    # copy over apk public keys
    keydir = rootp / "etc/apk/keys"

    shutil.rmtree(keydir, ignore_errors = True)
    keydir.mkdir(parents = True, exist_ok = True)

    for f in (paths.distdir() / "etc/keys").glob("*.pub"):
        shutil.copy2(f, keydir)

def repo_sync():
    confdir = paths.masterdir() / "etc/apk"
    confdir.mkdir(parents = True, exist_ok = True)

    repos_mdir = open(confdir / "repositories", "w")
    repos_hdir = open(paths.hostdir() / "repositories", "w")

    repos_mdir.write("# automatically generated apk repo list for chroot use\n")
    repos_hdir.write("# automatically generated apk repo list for host use\n")

    for f in (paths.distdir() / "etc/apk/repositories.d").glob("*.conf"):
        with open(f) as repof:
            for repo in repof:
                relpath = repo.lstrip("/")
                # in-chroot
                repos_mdir.write("/binpkgs/main/")
                repos_mdir.write(relpath)
                # out of chroot
                repos_hdir.write(str(paths.repository()))
                repos_hdir.write("/main/")
                repos_hdir.write(relpath)

    repos_mdir.close()
    repos_hdir.close()

    setup_keys(paths.masterdir())

    # do not refresh if chroot is not initialized
    if not (paths.masterdir() / ".cbuild_chroot_init").is_file():
        return

    if enter(
        "apk", ["update"], pretend_uid = 0, pretend_gid = 0,
        mount_binpkgs = True
    ).returncode != 0:
        logger.get().out_red(f"cbuild: failed to update pkg database")
        raise Exception()

def reconfigure():
    if not chroot_check():
        return

    statefile = paths.masterdir() / ".cbuild_chroot_configured"

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
        path = paths.masterdir()

    (path / "tmp").mkdir(parents = True, exist_ok = True)
    (path / "dev").mkdir(parents = True, exist_ok = True)
    (path / "etc/apk").mkdir(parents = True, exist_ok = True)
    (path / "usr/lib/apk/db").mkdir(parents = True, exist_ok = True)
    (path / "var/cache/apk").mkdir(parents = True, exist_ok = True)
    (path / "var/cache/misc").mkdir(parents = True, exist_ok = True)

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

    irun = subprocess.run([
        "apk", "add", "--root", paths.masterdir(), "--no-scripts",
        "--repositories-file", paths.hostdir() / "repositories",
        "--arch", arch, "base-chroot"
    ])
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
    if bootstrapping == None:
        bootstrapping = not (paths.masterdir() / ".cbuild_chroot_init").is_file()

    log = logger.get()

    log.out("cbuild: removing autodeps...")

    failed = False

    if subprocess.run([
        "apk", "info", "--allow-untrusted", "--installed", "--root",
        paths.masterdir(), "autodeps-host"
    ], capture_output = True).returncode == 0:
        if bootstrapping:
            del_ret = subprocess.run([
                "apk", "del", "--root", paths.masterdir(),
                "--no-scripts", "--repositories-file",
                paths.hostdir() / "repositories",
                "autodeps-host"
            ], capture_output = True)
        else:
            del_ret = enter(
                "apk", ["del", "autodeps-host"], capture_out = True,
                pretend_uid = 0, pretend_gid = 0, mount_binpkgs = True
            )

        if del_ret.returncode != 0:
            log.out_plain(">> stderr (host):")
            log.out_plain(del_ret.stderr.decode())
            failed = True

    if subprocess.run([
        "apk", "info", "--allow-untrusted", "--installed", "--root",
        paths.masterdir(), "autodeps-target"
    ], capture_output = True).returncode == 0:
        if bootstrapping:
            del_ret = subprocess.run([
                "apk", "del", "--root", paths.masterdir(),
                "--no-scripts", "--repositories-file",
                paths.hostdir() / "repositories",
                "autodeps-target"
            ], capture_output = True)
        else:
            del_ret = enter(
                "apk", ["del", "autodeps-target"], capture_out = True,
                pretend_uid = 0, pretend_gid = 0, mount_binpkgs = True
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

    logger.get().out("cbuild: updating software in %s masterdir..." \
        % str(paths.masterdir()))

    remove_autodeps(False)

    enter(
        "apk", ["update", "-q"], pretend_uid = 0, pretend_gid = 0,
        mount_binpkgs = True, check = True
    )
    enter(
        "apk", ["upgrade", "--available"],
        pretend_uid = 0, pretend_gid = 0, mount_binpkgs = True, check = True
    )

def enter(cmd, args = [], capture_out = False, check = False,
          env = {}, stdout = None, stderr = None, wrkdir = None,
          bootstrapping = False, ro_root = False, unshare_all = False,
          mount_binpkgs = False, mount_ccache = False,
          pretend_uid = None, pretend_gid = None, extra_path = None):
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

    if bootstrapping:
        return subprocess.run(
            [cmd] + args, env = envs,
            capture_output = capture_out, check = check,
            stdout = stdout, stderr = stderr,
            cwd = os.path.abspath(wrkdir) if wrkdir else None
        )

    bcmd = [
        "bwrap",
        root_bind, paths.masterdir(), "/",
        "--bind", paths.masterdir() / "builddir", "/builddir",
        "--bind", paths.masterdir() / "destdir", "/destdir",
        "--ro-bind", paths.hostdir() / "sources", "/sources",
        "--dev", "/dev",
        "--proc", "/proc",
        "--tmpfs", "/tmp",
    ]

    if mount_binpkgs:
        bcmd += ["--ro-bind", paths.repository(), "/binpkgs"]

    if mount_ccache:
        bcmd += ["--bind", paths.hostdir() / "ccache", "/ccache"]

    if pretend_uid != None:
        bcmd += ["--uid", str(pretend_uid)]
    if pretend_gid != None:
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
