from cbuild.core import logger, paths, chroot, profile

from . import sign as asign

import os
import pathlib
import subprocess

_use_net = True


def set_network(use_net):
    global _use_net
    _use_net = use_net


def collect_repos(mrepo, intree, arch, use_altrepo, use_stage, use_net):
    ret = []
    # sometimes we need no repos
    if not mrepo:
        return ret

    if isinstance(mrepo, str):
        srepos = [mrepo]
    elif isinstance(mrepo, list):
        srepos = mrepo
    else:
        srepos = mrepo.rparent.source_repositories

    if not arch:
        arch = chroot.host_cpu()

    prof = profile.get_profile(arch)
    use_cache = False

    rrepos = set(prof.repos)

    for r in chroot.get_confrepos():
        if not r.startswith("/"):
            # should be a remote repository, skip outright if we
            # know that remote repos will not be used during this run
            if not use_net:
                continue
            for cr in srepos:
                if cr not in rrepos:
                    continue
                ret.append("--repository")
                ret.append(r.replace("@section@", cr))
                use_cache = True
            continue
        r = r.lstrip("/")
        for cr in srepos:
            rl = r.replace("@section@", cr)
            rpath = paths.repository() / rl
            spath = paths.stage_repository() / rl
            # stage repo
            if use_stage:
                sbase = spath / arch
                sidx = sbase / "Packages.adb"
                if not sidx.is_file():
                    sidx = sbase / "APKINDEX.tar.gz"
                if sidx.is_file():
                    ret.append("--repository")
                    if intree:
                        ret.append(f"/stagepkgs/{rl}/{arch}/{sidx.name}")
                    else:
                        ret.append(str(sidx))
            # regular repo
            rbase = rpath / arch
            ridx = rbase / "Packages.adb"
            if not ridx.is_file():
                ridx = rbase / "APKINDEX.tar.gz"
            if ridx.is_file():
                ret.append("--repository")
                if intree:
                    ret.append(f"/binpkgs/{rl}/{arch}/{ridx.name}")
                else:
                    ret.append(str(ridx))

    # alt repository comes last in order to be lower priority
    # also, always ignore stage for altrepo, as it should be considered opaque
    if paths.alt_repository() and use_altrepo:
        for r in chroot.get_confrepos():
            if not r.startswith("/"):
                continue
            r = r.lstrip("/")
            for cr in srepos:
                rl = r.replace("@section@", cr)
                rpath = paths.alt_repository() / rl
                rbase = rpath / arch
                ridx = rbase / "Packages.adb"
                if not ridx.is_file():
                    ridx = rbase / "APKINDEX.tar.gz"
                if ridx.is_file():
                    ret.append("--repository")
                    if intree:
                        ret.append(f"/altbinpkgs/{rl}/{arch}/{ridx.name}")
                    else:
                        ret.append(str(ridx))

    if use_cache:
        ret.append("--cache-dir")
        cdir = paths.cbuild_cache() / "apk" / arch
        cdir.mkdir(exist_ok=True, parents=True)
        if intree:
            ret.append(f"/cbuild_cache/apk/{arch}")
        else:
            ret.append(str(cdir))

    return ret


def call(
    subcmd,
    args,
    mrepo,
    cwd=None,
    env=None,
    capture_output=False,
    root=None,
    arch=None,
    allow_untrusted=False,
    use_altrepo=True,
    use_stage=True,
    allow_network=True,
    return_repos=False,
):
    if allow_network:
        allow_network = _use_net
    cmd = [
        paths.apk(),
        subcmd,
        "--no-interactive",
        "--root",
        root if root else paths.bldroot(),
        "--repositories-file",
        "/dev/null",
    ]
    if arch:
        cmd += ["--arch", arch]
    if not allow_network:
        cmd += ["--no-network"]
    if allow_untrusted:
        cmd.append("--allow-untrusted")
    if subcmd in ["add", "del", "fix", "upgrade"]:
        cmd.append("--clean-protected")

    crepos = collect_repos(
        mrepo, False, arch, use_altrepo, use_stage, allow_network
    )

    retv = subprocess.run(
        cmd + crepos + args, cwd=cwd, env=env, capture_output=capture_output
    )
    if return_repos:
        return retv, crepos
    return retv


# should never be called during stage 0 builds, only with a real chroot
def call_chroot(
    subcmd,
    args,
    mrepo,
    capture_output=False,
    check=False,
    arch=None,
    allow_untrusted=False,
    use_stage=True,
    full_chroot=False,
    allow_network=True,
    return_repos=False,
):
    from cbuild.core import chroot

    if allow_network:
        allow_network = _use_net

    mount_cache = subcmd in ["add", "del", "fix", "update", "upgrade"]

    if full_chroot:
        cmd = [subcmd]
    else:
        cmd = [subcmd, "--repositories-file", "/dev/null"]
    cmd.append("--no-interactive")
    if arch:
        cmd += ["--arch", arch]
    if not allow_network:
        cmd += ["--no-network"]
    if allow_untrusted:
        cmd.append("--allow-untrusted")
    if mount_cache and subcmd != "update":
        cmd.append("--clean-protected")

    if not full_chroot:
        crepos = collect_repos(
            mrepo, True, arch, True, use_stage, allow_network
        )
    else:
        crepos = []

    cmd += crepos

    retv = chroot.enter(
        "apk",
        *cmd,
        *args,
        capture_output=capture_output,
        check=check,
        fakeroot=True,
        mount_binpkgs=True,
        mount_cbuild_cache=mount_cache,
    )
    if return_repos:
        return retv, crepos
    return retv


def is_installed(pkgn, pkg=None):
    cpf = pkg.rparent.profile() if pkg else None

    if pkg and cpf.cross:
        sysp = paths.bldroot() / cpf.sysroot.relative_to("/")
        aarch = cpf.arch
    else:
        sysp = paths.bldroot()
        aarch = None

    return (
        call(
            "info",
            ["--installed", pkgn],
            None,
            root=sysp,
            capture_output=True,
            arch=aarch,
            allow_untrusted=True,
        ).returncode
        == 0
    )


def get_provider(thing, pkg):
    cpf = pkg.rparent.profile() if pkg else None

    if pkg and cpf.cross:
        sysp = paths.bldroot() / cpf.sysroot.relative_to("/")
        aarch = cpf.arch
    else:
        sysp = paths.bldroot()
        aarch = None

    out = (
        call(
            "search",
            ["--from", "installed", "-q", "-e", thing],
            None,
            root=sysp,
            capture_output=True,
            arch=aarch,
            allow_untrusted=True,
        )
        .stdout.strip()
        .decode()
    )

    if len(out) == 0:
        return None

    return out


def check_version(*args):
    # buggy apk behavior
    if len(args) == 1 and not args[0][0].isdigit():
        return False
    v = subprocess.run(
        [paths.apk(), "version", "--quiet", "--check", *args],
        capture_output=True,
    )
    return v.returncode == 0


def compare_version(v1, v2, strict=True):
    if strict and not check_version(v1, v2):
        # this is more like an assertion, in cases where strict checking
        # is used this should never fire unless something is super wrong
        raise RuntimeError("invalid version")

    v = subprocess.run(
        [paths.apk(), "version", "--quiet", "--test", v1, v2],
        capture_output=True,
        check=True,
    ).stdout.strip()

    if v == b"=":
        return 0
    elif v == b"<":
        return -1
    else:
        return 1


def summarize_repo(repopath, olist, quiet=False):
    rtimes = {}
    obsolete = []

    for f in repopath.glob("*.apk"):
        fn = f.name
        pf = fn[:-4]
        rd = pf.rfind("-")
        if rd > 0:
            rd = pf.rfind("-", 0, rd)
        if rd < 0:
            if not quiet:
                logger.get().out(
                    f"\f[orange]WARNING: Malformed file name found, skipping: {fn}"
                )
            continue
        pn = pf[0:rd]
        mt = f.stat().st_mtime
        if pn not in rtimes:
            rtimes[pn] = (mt, f.name)
        else:
            omt, ofn = rtimes[pn]
            # this package is newer, so prefer it
            if mt > omt:
                fromf = ofn
                fromv = ofn[rd + 1 : -4]
                tof = f.name
                tov = pf[rd + 1 :]
                rtimes[pn] = (mt, f.name)
                obsolete.append(ofn)
            elif mt < omt:
                fromf = f.name
                fromv = pf[rd + 1 :]
                tof = ofn
                tov = ofn[rd + 1 : -4]
                obsolete.append(f.name)
            else:
                # same timestamp? should pretty much never happen
                # take the newer version anyway
                if compare_version(pf[rd + 1 :], ofn[rd + 1 : -4]) > 0:
                    rtimes[pn] = (mt, f.name)
                    obsolete.append(ofn)
                else:
                    obsolete.append(f.name)
                continue

            if compare_version(tov, fromv, False) < 0 and not quiet:
                logger.get().out(
                    f"\f[orange]WARNING: Using lower version ({fromf} => {tof}): newer timestamp..."
                )

    for k, v in rtimes.items():
        olist.append(v[1])

    return obsolete


def prune(repopath, arch=None, dry=False):
    from cbuild.core import chroot

    if not arch:
        arch = chroot.host_cpu()

    repopath = repopath / arch

    if not repopath.is_dir():
        return

    logger.get().out(f"pruning old packages: {repopath}")

    nlist = []
    olist = summarize_repo(repopath, nlist, True)

    for pkg in olist:
        print(f"pruning: {pkg}")
        if not dry:
            (repopath / pkg).unlink()

    logger.get().out("repo cleanup complete")


def find_indexes(repopath):
    for root, dirs, files in repopath.walk():
        has_adb = False
        has_gz = False
        for fl in files:
            if fl == "Packages.adb":
                has_adb = True
                if has_gz:
                    break
            elif fl == "APKINDEX.tar.gz":
                has_gz = True
                if has_adb:
                    break
        if not has_adb and not has_gz:
            continue
        if has_adb:
            yield repopath / root / "Packages.adb"
        else:
            yield repopath / root / "APKINDEX.tar.gz"


def build_index(repopath, epoch, allow_untrusted=False):
    repopath = pathlib.Path(repopath)

    aargs = ["--quiet", "--output", "Packages.adb", "--hash", "sha256-160"]

    if (repopath / "Packages.adb").is_file():
        aargs += ["--index", "Packages.adb"]
    elif (repopath / "APKINDEX.tar.gz").is_file():
        aargs += ["--index", "APKINDEX.tar.gz"]

    keypath = None
    if not allow_untrusted:
        keypath = asign.get_keypath()

    if keypath:
        aargs += ["--sign-key", keypath]

    aenv = {"PATH": os.environ["PATH"], "SOURCE_DATE_EPOCH": str(epoch)}

    ilen = len(aargs)

    summarize_repo(repopath, aargs)

    # no packages, just drop the index
    if (len(aargs) - ilen) == 0:
        (repopath / "APKINDEX.tar.gz").unlink(missing_ok=True)
        (repopath / "Packages.adb").unlink(missing_ok=True)
        return True

    signr = call(
        "mkndx",
        aargs,
        None,
        cwd=repopath,
        env=aenv,
        allow_untrusted=not keypath,
    )
    if signr.returncode != 0:
        logger.get().out("\f[red]Indexing failed!")
        return False

    # for compatibility
    lidx = repopath / "APKINDEX.tar.gz"
    lidx.unlink(missing_ok=True)
    lidx.hardlink_to(repopath / "Packages.adb")

    return True


def get_arch():
    sr = subprocess.run([paths.apk(), "--print-arch"], capture_output=True)
    if sr.returncode != 0:
        return None
    rs = sr.stdout.strip().decode()
    if not rs or len(rs) == 0:
        return None
    return rs
