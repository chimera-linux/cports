from cbuild.core import chroot, logger, paths, version

from . import sign

import os
import pathlib
import subprocess

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
                logger.get().warn(f"Malformed file name found, skipping: {str(fn)}")
            continue
        pn = pf[0:rd]
        mt = os.path.getmtime(f)
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
                if version.compare(pf[rd + 1:], ofn[rd + 1:-4]) > 0:
                    rtimes[pn] = (mt, f.name)
                    obsolete.append(ofn)
                else:
                    obsolete.append(f.name)

            if version.compare(tov, fromv) < 0 and not quiet:
                logger.get().warn(f"Using lower version ({fromf} => {tof}): newer timestamp...")

    for k, v in rtimes.items():
        olist.append(v[1])

    return obsolete

def prune(repopath):
    repopath = repopath / chroot.target_cpu()

    if not repopath.is_dir():
        return

    logger.get().out(f"pruning old packages: {str(repopath)}")

    nlist = []
    olist = summarize_repo(repopath, nlist, True)

    for pkg in olist:
        print(f"pruning: {pkg}")
        (repopath / pkg).unlink()

    logger.get().out("repo cleanup complete")

def build_index(repopath, epoch, keypath):
    repopath = pathlib.Path(repopath)

    cmd = ["apk", "index", "--quiet", "--root", str(paths.masterdir())]

    if (repopath / "APKINDEX.tar.gz").is_file():
        cmd += ["--index", "APKINDEX.tar.gz"]

    # if no key is given, just use the final index name
    if not keypath:
        cmd += ["--allow-untrusted", "--output", "APKINDEX.tar.gz"]
    else:
        cmd += ["--output", "APKINDEX.unsigned.tar.gz"]

    summarize_repo(repopath, cmd)

    # create unsigned index
    signr = subprocess.run(cmd, cwd = repopath, env = {
        "PATH": os.environ["PATH"],
        "SOURCE_DATE_EPOCH": str(epoch)
    })
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
