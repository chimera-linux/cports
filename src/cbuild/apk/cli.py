from cbuild.core import logger, paths

from . import sign

import os
import pathlib
import subprocess

_use_net = True

def set_network(use_net):
    global _use_net
    _use_net = use_net

def _collect_repos(mrepo, intree, arch, use_altrepo = True, use_stage = True):
    from cbuild.core import chroot

    ret = []
    # sometimes we need no repos
    if not mrepo:
        return ret

    if isinstance(mrepo, str):
        srepos = [mrepo]
    else:
        srepos = mrepo.rparent.source_repositories

    if not arch:
        arch = chroot.host_cpu()

    for r in chroot.get_confrepos():
        if not r.startswith("/"):
            # should be a remote repository, skip outright if we
            # know that remote repos will not be used during this run
            if _use_net:
                ret.append(r)
            continue
        r = r.lstrip("/")
        for cr in srepos:
            rpath = paths.repository() / cr / r
            spath = rpath / ".stage"
            if (rpath / arch / "APKINDEX.tar.gz").is_file():
                ret.append("--repository")
                if intree:
                    ret.append(f"/binpkgs/{cr}/{r}")
                else:
                    ret.append(str(rpath))
            if (spath / arch / "APKINDEX.tar.gz").is_file() and use_stage:
                ret.append("--repository")
                if intree:
                    ret.append(f"/binpkgs/{cr}/{r}/.stage")
                else:
                    ret.append(str(spath))

    if not paths.alt_repository() or not use_altrepo:
        return ret

    # append alt repository to the end
    for r in chroot.get_confrepos():
        if not r.startswith("/"):
            continue
        r = r.lstrip("/")
        for cr in srepos:
            rpath = paths.alt_repository() / cr / r
            spath = rpath / ".stage"
            if (rpath / arch / "APKINDEX.tar.gz").is_file():
                ret.append("--repository")
                if intree:
                    ret.append(f"/altbinpkgs/{cr}/{r}")
                else:
                    ret.append(str(rpath))
            if (spath / arch / "APKINDEX.tar.gz").is_file() and use_stage:
                ret.append("--repository")
                if intree:
                    ret.append(f"/binpkgs/{cr}/{r}/.stage")
                else:
                    ret.append(str(spath))

    return ret

def call(
    subcmd, args, mrepo, cwd = None, env = None,
    capture_output = False, root = None, arch = None,
    allow_untrusted = False, use_altrepo = True,
    use_stage = True, fakeroot = False
):
    cmd = [
        "apk", subcmd, "--root", root if root else paths.bldroot(),
        "--repositories-file", "/dev/null",
    ]
    if arch:
        cmd += ["--arch", arch]
    if not _use_net:
        cmd += ["--no-network"]
    if allow_untrusted:
        cmd.append("--allow-untrusted")

    if fakeroot:
        if env:
            env = dict(env)
        else:
            env = {}
        env["FAKEROOTDONTTRYCHOWN"] = "1"
        cmd = ["fakeroot", "--"] + cmd

    return subprocess.run(
        cmd + _collect_repos(mrepo, False, arch, use_altrepo, use_stage) + args,
        cwd = cwd, env = env, capture_output = capture_output
    )

def call_chroot(
    subcmd, args, mrepo, capture_out = False, check = False, arch = None,
    allow_untrusted = False, use_stage = True
):
    from cbuild.core import chroot

    cmd = [subcmd, "--repositories-file", "/dev/null"]
    if arch:
        cmd += ["--arch", arch]
    if not _use_net:
        cmd += ["--no-network"]
    if allow_untrusted:
        cmd.append("--allow-untrusted")

    return chroot.enter(
        "apk", cmd + _collect_repos(mrepo, True, arch, use_stage) + args,
        capture_out = capture_out, check = check,
        fakeroot = True, mount_binpkgs = True
    )

def is_installed(pkgn, pkg = None):
    cpf = pkg.rparent.profile() if pkg else None

    if pkg and cpf.cross:
        sysp = paths.bldroot() / cpf.sysroot.relative_to("/")
        aarch = cpf.arch
    else:
        sysp = paths.bldroot()
        aarch = None

    return call(
        "info", ["--installed", pkgn], None, root = sysp,
        capture_output = True, arch = aarch, allow_untrusted = True
    ).returncode == 0

def get_provider(thing, pkg):
    cpf = pkg.rparent.profile() if pkg else None

    if pkg and cpf.cross:
        sysp = paths.bldroot() / cpf.sysroot.relative_to("/")
        aarch = cpf.arch
    else:
        sysp = paths.bldroot()
        aarch = None

    out = call(
        "search", ["-q", "-e", thing], pkg, root = sysp,
        capture_output = True, arch = aarch, allow_untrusted = True
    ).stdout.strip().decode()

    if len(out) == 0:
        return None

    return out

def check_version(*args):
    v = subprocess.run(
        ["apk", "version", "--quiet", "--check", *args],
        capture_output = True
    )
    return v.returncode == 0

def compare_version(v1, v2, strict = True):
    if strict and not check_version(v1, v2):
        raise Exception("invalid version")

    v = subprocess.run(
        ["apk", "version", "--quiet", "--test", v1, v2],
        capture_output = True, check = True
    ).stdout.strip()

    if v == b"=":
        return 0
    elif v == b"<":
        return -1
    else:
        return 1

def summarize_repo(repopath, olist, quiet = False):
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
                logger.get().warn(f"Malformed file name found, skipping: {fn}")
            continue
        pn = pf[0:rd]
        mt = f.stat().st_mtime
        if not pn in rtimes:
            rtimes[pn] = (mt, f.name)
        else:
            omt, ofn = rtimes[pn]
            # this package is newer, so prefer it
            if mt > omt:
                fromf = ofn
                fromv = ofn[rd + 1:-4]
                tof = f.name
                tov = pf[rd + 1:]
                rtimes[pn] = (mt, f.name)
                obsolete.append(ofn)
            elif mt < omt:
                fromf = f.name
                fromv = pf[rd + 1:]
                tof = ofn
                tov = ofn[rd + 1:-4]
                obsolete.append(f.name)
            else:
                # same timestamp? should pretty much never happen
                # take the newer version anyway
                if compare_version(pf[rd + 1:], ofn[rd + 1:-4]) > 0:
                    rtimes[pn] = (mt, f.name)
                    obsolete.append(ofn)
                else:
                    obsolete.append(f.name)

            if compare_version(tov, fromv) < 0 and not quiet:
                logger.get().warn(f"Using lower version ({fromf} => {tof}): newer timestamp...")

    for k, v in rtimes.items():
        olist.append(v[1])

    return obsolete

def prune(repopath, arch = None):
    from cbuild.core import chroot

    if not arch:
        arch = chroot.target_cpu()

    repopath = repopath / arch

    if not repopath.is_dir():
        return

    logger.get().out(f"pruning old packages: {repopath}")

    nlist = []
    olist = summarize_repo(repopath, nlist, True)

    for pkg in olist:
        print(f"pruning: {pkg}")
        (repopath / pkg).unlink()

    logger.get().out("repo cleanup complete")

def build_index(repopath, epoch, keypath):
    repopath = pathlib.Path(repopath)

    aargs = ["--quiet"]

    if (repopath / "APKINDEX.tar.gz").is_file():
        aargs += ["--index", "APKINDEX.tar.gz"]

    # if no key is given, just use the final index name
    if not keypath:
        aargs += ["--output", "APKINDEX.tar.gz"]
    else:
        aargs += ["--output", "APKINDEX.unsigned.tar.gz"]

    summarize_repo(repopath, aargs)

    # create unsigned index
    signr = call("index", aargs, None, cwd = repopath, env = {
        "PATH": os.environ["PATH"],
        "SOURCE_DATE_EPOCH": str(epoch)
    }, allow_untrusted = not keypath)
    if signr.returncode != 0:
        logger.get().out_red("Indexing failed!")
        return False

    # we're done if no key is given
    if not keypath:
        return True

    try:
        signhdr = sign.sign(
            keypath, repopath / "APKINDEX.unsigned.tar.gz", epoch
        )
    except:
        return False

    # write signed index
    with open(repopath / "APKINDEX.tar.gz", "wb") as outf:
        outf.write(signhdr)
        with open(repopath / "APKINDEX.unsigned.tar.gz", "rb") as inf:
            while True:
                buf = inf.read(16 * 1024)
                if not buf:
                    break
                outf.write(buf)
        (repopath / "APKINDEX.unsigned.tar.gz").unlink()

    return True
