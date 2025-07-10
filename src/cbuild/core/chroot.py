import subprocess
import os
import re
import time
import errno
import shutil
import pathlib
import binascii
from tempfile import mkstemp, mkdtemp

from cbuild.core import logger, paths, errors
from cbuild.apk import cli as apki, sign as signi
from cbuild.util import flock

_chroot_checked = False
_chroot_ready = False
_extra_pkgs = []


def host_cpu():
    return _host


def set_host(tgt):
    global _host
    _host = tgt


def _chroot_check(error):
    if error and not _chroot_ready:
        raise errors.CbuildException(
            "working bldroot is required for this step (try binary-bootstrap)"
        )
    return _chroot_ready


def chroot_check(force=False, error=True):
    global _chroot_checked, _chroot_ready

    if _chroot_checked and not force:
        return _chroot_check(error)

    _chroot_checked = True

    if (paths.bldroot() / ".cbuild_chroot_init").is_file():
        _chroot_ready = True
        cpun = (paths.bldroot() / ".cbuild_chroot_init").read_text().strip()
        set_host(cpun)
    else:
        _chroot_ready = False

    return _chroot_check(error)


def set_extras(elist):
    global _extra_pkgs

    _extra_pkgs = ["base-cbuild", *elist]


def get_world_base():
    return _extra_pkgs


def _subst_in(pat, rep, src, dest=None):
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


def _prepare_etc():
    bfp = paths.distdir() / "main/base-files/files"
    tfp = paths.bldroot() / "etc"

    shutil.copy(bfp / "etc/passwd", tfp)
    shutil.copy(bfp / "etc/group", tfp)

    (paths.bldroot() / "etc/resolv.conf").unlink(missing_ok=True)
    shutil.copy("/etc/resolv.conf", paths.bldroot() / "etc")

    with open(tfp / "passwd", "a") as pf:
        pf.write("cbuild:x:1337:1337:cbuild user:/tmp:/bin/nologin\n")

    with open(tfp / "group", "a") as pf:
        pf.write("cbuild:x:1337:\n")

    # machine-id for cbuild
    with open(tfp / "machine-id", "w") as mf:
        mf.write("e91d1c901dd8d2509161fd9b548b54f5\n")

    # terminfo in case it's missing so host TERM works inside the bldroot
    if "TERM" in os.environ:
        tinfo = os.environ["TERM"]
        if len(tinfo) > 0:
            tpath = f"usr/share/terminfo/{tinfo[0]}/{tinfo}"
            spath = pathlib.Path("/") / tpath
            dpath = paths.bldroot() / tpath
            if not dpath.exists() and spath.exists():
                dpath.parent.mkdir(0o755, parents=True, exist_ok=True)
                shutil.copy(spath, dpath.parent)

    # delete potential shadow so sysusers does not fail
    (tfp / "shadow").unlink(missing_ok=True)
    # delete potential previous cbuild file so we are clean
    (paths.bldroot() / "usr/lib/sysusers.d/cbuild.conf").unlink(missing_ok=True)

    # Create groups for the chroot
    if (paths.bldroot() / "usr/bin/sd-sysusers").is_file():
        enter("sd-sysusers", capture_output=True, check=True)


def _init():
    xdir = paths.bldroot() / "etc" / "apk"
    xdir.mkdir(parents=True, exist_ok=True)

    # generate machine-id
    with open(paths.bldroot() / "etc/machine-id", "wb") as mid:
        mid.write(b"%s\n" % binascii.b2a_hex(os.urandom(16)))


def _prepare():
    sfpath = paths.bldroot() / ".cbuild_chroot_init"
    if sfpath.is_file():
        return
    if not (paths.bldroot() / "usr" / "bin" / "sh").is_file():
        raise errors.CbuildException("bootstrap not installed, can't continue")

    (paths.bldroot() / "etc" / "localtime").symlink_to(
        "../usr/share/zoneinfo/UTC"
    )

    _prepare_etc()

    # Create temporary files for the chroot
    if (paths.bldroot() / "usr/bin/sd-tmpfiles").is_file():
        enter("sd-tmpfiles", "--create", fakeroot=True)

    if (paths.bldroot() / "usr/bin/update-ca-certificates").is_file():
        enter("update-ca-certificates")

    with open(sfpath, "w") as sf:
        sf.write(host_cpu() + "\n")


def setup_keys(rootp):
    # copy over apk public keys
    keydir = rootp / "etc/apk/keys"

    shutil.rmtree(keydir, ignore_errors=True)
    keydir.mkdir(parents=True, exist_ok=True)

    for f in (paths.distdir() / "etc/apk/keys").glob("*.pub"):
        shutil.copy2(f, keydir)

    for f in paths.keys().glob("*.pub"):
        shutil.copy2(f, keydir)

    pkey = signi.get_keypath()
    if pkey:
        pubkey = pkey.with_suffix(pkey.suffix + ".pub")
        if pubkey.is_file():
            shutil.copy2(pubkey, keydir)


_crepos = None
_mirror = None
_depcheck = True


def set_mirror(mirror):
    global _mirror
    _mirror = mirror


def set_depcheck(depcheck):
    global _depcheck
    _depcheck = depcheck


def get_depcheck():
    return _depcheck


def get_confrepos():
    global _crepos

    if _crepos:
        return _crepos

    _crepos = []
    for f in (paths.distdir() / "etc/apk/repositories.d").glob("*.conf"):
        with open(f) as repof:
            for repo in repof:
                _crepos.append(repo.strip().replace("@mirror@", _mirror))

    return _crepos


def repo_init():
    setup_keys(paths.bldroot())

    apkpath = paths.bldroot() / "etc/apk"

    rfile = apkpath / "repositories"
    rfile.unlink(missing_ok=True)

    cfile = apkpath / "cache"
    cfile.unlink(missing_ok=True)

    shutil.rmtree(paths.bldroot() / "var/cache/apk", ignore_errors=True)

    return rfile, cfile


def shell_update(rnet, dirty):
    hcpu = host_cpu()
    rfile, cfile = repo_init()
    with rfile.open("w") as rfh:
        for rd in paths.repository().iterdir():
            for cr in get_confrepos():
                if not cr.startswith("/"):
                    continue
                cr = cr.lstrip("/").replace("@section@", rd.name)
                idxp = rd.parent / cr / hcpu
                if (idxp / "Packages.adb").is_file():
                    rfh.write(f"v3 /binpkgs/{cr}\n")
                elif (idxp / "APKINDEX.tar.gz").is_file():
                    rfh.write(f"v2 /binpkgs/{cr}\n")
        if paths.alt_repository():
            for rd in paths.alt_repository().iterdir():
                for cr in get_confrepos():
                    if not cr.startswith("/"):
                        continue
                    cr = cr.lstrip("/").replace("@section@", rd.name)
                    idxp = rd.parent / cr / hcpu
                    if (idxp / "Packages.adb").is_file():
                        rfh.write(f"v3 /altbinpkgs/{cr}\n")
                    elif (idxp / "APKINDEX.tar.gz").is_file():
                        rfh.write(f"v2 /altbinpkgs/{cr}\n")
        # remote repos come last
        if rnet:
            from cbuild.core import profile

            for rd in profile.get_profile(hcpu).repos:
                for cr in get_confrepos():
                    if cr.startswith("/"):
                        continue
                    rfh.write(cr.replace("@section@", rd))
                    rfh.write("\n")

    # ensure any local apk commands can write into cache
    (paths.cbuild_cache() / "apk" / hcpu).mkdir(parents=True, exist_ok=True)
    cfile.symlink_to(f"/cbuild_cache/apk/{hcpu}")

    if dirty:
        return

    with flock.lock(flock.apklock(hcpu)):
        if (
            apki.call_chroot(
                "update", [], None, full_chroot=True, allow_network=rnet
            ).returncode
            != 0
        ):
            raise errors.CbuildException("failed to update pkg database")


def initdb(path=None):
    # we init the database ourselves
    if not path:
        path = paths.bldroot()

    (path / "tmp").mkdir(parents=True, exist_ok=True)
    (path / "dev").mkdir(parents=True, exist_ok=True)
    (path / "etc/apk").mkdir(parents=True, exist_ok=True)
    (path / "usr/lib/apk/db").mkdir(parents=True, exist_ok=True)
    (path / "var/cache/apk").mkdir(parents=True, exist_ok=True)
    (path / "var/cache/misc").mkdir(parents=True, exist_ok=True)
    (path / "var/log").mkdir(parents=True, exist_ok=True)

    # largely because of custom usrmerge
    if not (path / "lib").is_symlink():
        (path / "lib").symlink_to("usr/lib")

    (path / "usr/lib/apk/db/installed").touch()
    (path / "etc/apk/world").touch()


def install():
    if chroot_check(error=False):
        return

    from cbuild.core import template

    logger.get().out(f"cbuild: installing {' '.join(_extra_pkgs)}...")

    initdb()

    setup_keys(paths.bldroot())

    lkp = flock.apklock(host_cpu())
    lkp.parent.mkdir(parents=True, exist_ok=True)

    with flock.lock(lkp):
        irun = apki.call(
            "add",
            ["--usermode", "--no-scripts", *_extra_pkgs],
            template.get_cats(),
            arch=host_cpu(),
        )

    if irun.returncode != 0:
        raise errors.CbuildException("failed to install container packages")

    logger.get().out("cbuild: container set up successfully!")

    paths.prepare()
    _prepare()
    chroot_check(True, False)
    _init()


def get_fakeroot(bootstrap):
    inp = paths.cbuild() / "misc/fakeroot.sh"

    if bootstrap:
        return inp

    rp = paths.bldroot() / ".cbuild_fakeroot.sh"

    if rp.is_file():
        return "/.cbuild_fakeroot.sh"

    rp.unlink(missing_ok=True)
    shutil.copyfile(inp, rp)

    return "/.cbuild_fakeroot.sh"


def _setup_dummy(rootp, archn):
    tmpd = mkdtemp()
    tmpd = pathlib.Path(tmpd)

    pkgn = "base-cross-target-meta"
    pkgv = "0.1-r0"
    repod = tmpd / archn
    repod.mkdir()

    epoch = int(time.time())

    logger.get().out(f"cbuild: installing virtual provider for {archn}...")

    # generate exact provided versions
    #
    # this is necessary because if any other versions are provided, it will
    # cause problems with some makedepends (e.g. static libraries for musl,
    # libunwind and so on depend on exact versions of their devel packages)

    from cbuild.core import template

    def _get_ver(pkgn):
        tobj = template.Template(
            f"main/{pkgn}",
            archn,
            True,
            False,
            (1, 1),
            False,
            False,
            None,
        )
        return f"{tobj.pkgver}-r{tobj.pkgrel}"

    fortify_ver = _get_ver("fortify-headers")
    atomic_ver = _get_ver("libatomic-chimera")
    files_ver = _get_ver("base-files")
    musl_ver = _get_ver("musl")
    llvm_ver = _get_ver("llvm")

    provides = [
        f"base-files={files_ver}",
        f"fortify-headers={fortify_ver}",
        f"libatomic-chimera={atomic_ver}",
        f"libatomic-chimera-devel={atomic_ver}",
        f"musl={musl_ver}",
        f"musl-devel={musl_ver}",
        f"libcxx={llvm_ver}",
        f"libcxx-devel={llvm_ver}",
        f"libcxxabi={llvm_ver}",
        f"libcxxabi-devel={llvm_ver}",
        f"libunwind={llvm_ver}",
        f"libunwind-devel={llvm_ver}",
        "so:libc.so=0",
        "so:libc++abi.so.1=1.0",
        "so:libc++.so.1=1.0",
        "so:libatomic.so.1=1.69.0",
        "so:libunwind.so.1=1.0",
    ]

    try:
        ret = apki.call(
            "mkpkg",
            [
                "--output",
                repod / f"{pkgn}-{pkgv}.apk",
                "--info",
                f"name:{pkgn}",
                "--info",
                f"version:{pkgv}",
                "--info",
                "description:Target sysroot virtual provider",
                "--info",
                f"arch:{archn}",
                "--info",
                f"origin:{pkgn}",
                "--info",
                "url:https://chimera-linux.org",
                "--info",
                f"build-time:{int(epoch)}",
                "--info",
                f"provides:{' '.join(provides)}",
            ],
            None,
            root=rootp,
            capture_output=True,
            arch=archn,
            allow_untrusted=True,
        )
        if ret.returncode != 0:
            outl = ret.stderr.strip().decode()
            if len(outl) > 0:
                logger.get().out_plain(">> stderr:")
                logger.get().out_plain(outl)
            raise errors.CbuildException(
                f"failed to create virtual provider for {archn}"
            )

        if not apki.build_index(repod, epoch, True):
            raise errors.CbuildException(
                f"failed to index virtual provider for {archn}"
            )

        ret = apki.call(
            "add",
            ["--no-scripts", "--usermode", "--repository", tmpd, pkgn],
            None,
            root=rootp,
            capture_output=True,
            arch=archn,
            allow_untrusted=True,
        )

        if ret.returncode != 0:
            outl = ret.stderr.strip().decode()
            if len(outl) > 0:
                logger.get().out_plain(">> stderr:")
                logger.get().out_plain(outl)
            raise errors.CbuildException(
                f"failed to install virtual provider for {archn}"
            )
    finally:
        shutil.rmtree(tmpd)


def _prepare_arch(prof, dirty):
    rootp = paths.bldroot() / prof.sysroot.relative_to("/")
    # drop the whole thing
    if rootp.exists() and not dirty:
        logger.get().out(f"cbuild: clearing sysroot for {prof.arch}...")
        shutil.rmtree(rootp)

    # clear world so cross sysroot gets set up from scratch
    # this is a slow path but nobody cares about cross so whatever
    if not dirty:
        cleanup_world(False)

    logger.get().out(f"setting up sysroot for {prof.arch}...")
    initdb(rootp)
    setup_keys(rootp)
    if not dirty:
        _setup_dummy(rootp, prof.arch)


def prepare_arch(arch, dirty):
    paths.prepare()

    if not arch:
        return

    from cbuild.core import profile

    prof = profile.get_profile(arch)

    if not prof.cross:
        return

    _prepare_arch(prof, dirty)


def cleanup_world(bootstrapping, prof=None, perform=True):
    from cbuild.core import template

    if bootstrapping is None:
        bootstrapping = not (paths.bldroot() / ".cbuild_chroot_init").is_file()

    log = logger.get()

    log.out("cbuild: cleaning world...")

    # best way to ensure everything is clean in stage 0
    if bootstrapping:
        # we need to keep builddir as that holds our state (logs etc)
        # everything else is handled by paths.prepare() and others
        for d in paths.bldroot().iterdir():
            if d.name == "builddir":
                continue
            if d.is_dir() and not d.is_symlink():
                shutil.rmtree(d)
            else:
                d.unlink()
        paths.prepare()
        initdb()
        repo_init()
        return

    paths.prepare()

    # in some cases we want to bail early without dealing with world at all
    if not perform:
        return

    # clean world
    old_world = set()
    new_world = set()

    with open(paths.bldroot() / "etc/apk/world", "r") as inf:
        for ln in inf:
            old_world.add(ln.strip())

    for ep in _extra_pkgs:
        new_world.add(ep)

    old_wlist = sorted(old_world)
    new_wlist = sorted(new_world)

    remlist = []
    addlist = []
    for x in old_wlist:
        if x not in new_world:
            remlist.append(x)
    for x in new_wlist:
        if x not in old_world:
            addlist.append(x)

    if len(remlist) > 0:
        log.out("\f[red]  " + " ".join(map(lambda x: f"-{x}", remlist)))
    if len(addlist) > 0:
        log.out("\f[green]  " + " ".join(map(lambda x: f"+{x}", addlist)))

    with open(paths.bldroot() / "etc/apk/world", "w") as outf:
        for ep in new_wlist:
            outf.write(f"{ep}\n")

    # perform transaction
    f_ret = apki.call_chroot(
        "fix",
        [],
        template.get_cats(),
        capture_output=True,
        allow_untrusted=True,
    )

    if f_ret.returncode != 0:
        log.out_plain(">> stderr (host):")
        log.out_plain(f_ret.stderr.decode())

    if prof and prof.cross:
        _prepare_arch(prof, False)

    if f_ret.returncode != 0:
        raise errors.CbuildException("failed to remove autodeps")


def update(pkg):
    chroot_check()

    logger.get().out(
        f"cbuild: updating software in {paths.bldroot()!s} container..."
    )

    paths.prepare()
    repo_init()

    # reinit passwd/group
    _prepare_etc()

    with flock.lock(flock.apklock(host_cpu())):
        apki.call_chroot("update", ["-q"], pkg, check=True, use_stage=True)
        apki.call_chroot(
            "upgrade", ["--available"], pkg, check=True, use_stage=True
        )

    # this is bootstrap-update
    if isinstance(pkg, str):
        return

    prof = pkg.profile()

    # not cross, so we don't care
    if not prof.cross:
        return

    rootp = paths.bldroot() / prof.sysroot.relative_to("/")

    # otherwise also update indexes in cross root
    with flock.lock(flock.apklock(prof.arch)):
        if (
            apki.call(
                "update", ["-q"], pkg, root=rootp, arch=prof.arch
            ).returncode
            != 0
        ):
            raise errors.CbuildException("failed to update cross pkg database")


def enter(
    cmd,
    *args,
    capture_output=False,
    check=False,
    env=None,
    stdout=None,
    stderr=None,
    input=None,
    wrkdir=None,
    bootstrapping=False,
    ro_root=False,
    ro_build=False,
    ro_dest=True,
    unshare_all=False,
    mount_binpkgs=False,
    mount_cbuild_cache=False,
    mount_cports=False,
    fakeroot=False,
    new_session=True,
    binpkgs_rw=False,
    tmpfiles=None,
    binpath=None,
    lldargs=None,
    term=False,
):
    defpath = []
    if binpath:
        defpath += binpath
    if bootstrapping:
        defpath += [os.environ["PATH"]]
    else:
        defpath += ["/usr/bin"]

    from cbuild.core import profile

    hprof = profile.get_profile(host_cpu())

    if not env:
        env = {}

    envs = {
        "PATH": ":".join(map(lambda v: str(v), defpath)),
        "SHELL": "/bin/sh",
        "HOME": "/tmp",
        "USER": "root" if fakeroot else "cbuild",
        "LC_COLLATE": "C",
        "LANG": "C.UTF-8",
        **env,
    }

    # propagate outside TERM and stuff into the chroot
    if term:
        if "TERM" in os.environ:
            envs["TERM"] = os.environ["TERM"]
        if "COLORTERM" in os.environ and logger.get().use_colors:
            envs["COLORTERM"] = os.environ["COLORTERM"]

    if hprof.wordsize == 32:
        kpers = "linux32"
    else:
        kpers = "linux64"

    if not unshare_all:
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
            [cmd, *args],
            env=envs,
            capture_output=capture_output,
            check=check,
            stdout=stdout,
            stderr=stderr,
            input=input,
            cwd=os.path.abspath(wrkdir) if wrkdir else None,
        )

    # we need to resolve it externally to not get
    # affected by the PATH we set for sandbox usage
    bwrap = shutil.which(paths.bwrap())
    if not bwrap:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), paths.bwrap()
        )

    bcmd = [
        bwrap,
        "--unshare-all",
        "--hostname",
        "cbuild",
        root_bind,
        paths.bldroot(),
        "/",
        build_bind,
        paths.builddir() / "builddir",
        "/builddir",
        dest_bind,
        paths.builddir() / "destdir",
        "/destdir",
        "--ro-bind",
        paths.sources(),
        "/sources",
        "--dev",
        "/dev",
        "--proc",
        "/proc",
        "--tmpfs",
        "/run",
        "--tmpfs",
        "/tmp",
        "--tmpfs",
        "/var/tmp",
    ]

    if new_session:
        bcmd += ["--new-session", "--die-with-parent"]

    if mount_binpkgs:
        bcmd += [
            "--ro-bind" if not binpkgs_rw else "--bind",
            paths.repository(),
            "/binpkgs",
            "--ro-bind" if not binpkgs_rw else "--bind",
            paths.stage_repository(),
            "/stagepkgs",
        ]
        if paths.alt_repository():
            bcmd += ["--ro-bind", paths.alt_repository(), "/altbinpkgs"]

    if mount_cbuild_cache:
        bcmd += ["--bind", paths.cbuild_cache(), "/cbuild_cache"]

    # always bubblewrap as cbuild user
    # root-needing things are done through fakeroot so we can chown
    bcmd += ["--uid", "1337"]
    bcmd += ["--gid", "1337"]

    if not unshare_all:
        bcmd += ["--share-net"]

    if wrkdir:
        bcmd.append("--chdir")
        bcmd.append(wrkdir)

    # extra file descriptors to pass to sandbox and bind to a file
    fdlist = []

    for tmpf in tmpfiles or []:
        # reopen as file descriptor to pass
        tmpfd = os.open(tmpf, os.O_RDONLY)
        fdlist.append(tmpfd)
        bcmd += ["--ro-bind-data", str(tmpfd), f"/tmp/{tmpf.name}"]

    if lldargs:
        rfd, wfd = os.pipe()
        os.write(wfd, "\n".join(lldargs).encode())
        os.close(wfd)
        fdlist.append(rfd)
        bcmd += ["--ro-bind-data", str(rfd), "/tmp/cbuild-lld-args"]

    if fakeroot:
        bcmd += [
            "--setenv",
            "FAKEROOTDONTTRYCHOWN",
            "1",
            "--",
            kpers,
            "sh",
            get_fakeroot(False),
        ]
    else:
        bcmd += [kpers, "--"]

    bcmd.append(cmd)
    bcmd += args

    try:
        return subprocess.run(
            bcmd,
            env=envs,
            capture_output=capture_output,
            check=check,
            stdout=stdout,
            stderr=stderr,
            input=input,
            pass_fds=tuple(fdlist),
        )
    finally:
        for fd in fdlist:
            os.close(fd)
