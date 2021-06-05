from cbuild.core import paths
import os
import hashlib
from urllib import request

def get_cksum(fname, dfile, pkg):
    with open(dfile, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
    pkg.error(f"cannot get checksum of '{fname}'")

def verify_cksum(fname, dfile, cksum, pkg):
    pkg.log(f"verifying checksum for distfile '{fname}'... ", "")
    filesum = get_cksum(fname, dfile, pkg)
    if cksum != filesum:
        pkg.logger.out_plain("")
        pkg.logger.out_red(f"SHA256 mismatch for '{fname}':\n@{filesum}")
        return False
    else:
        shapath = os.path.join(paths.sources(), "by_sha256")
        linkpath = os.path.join(shapath, f"{cksum}_{fname}")
        if not os.path.isfile(linkpath):
            os.makedirs(shapath, exist_ok = True)
            os.link(dfile, linkpath)
        pkg.logger.out_plain("OK.")

def link_cksum(fname, dfile, cksum, pkg):
    shapath = os.path.join(paths.sources(), "by_sha256")
    linkpath = os.path.join(shapath, f"{cksum}_{fname}")
    if len(cksum) > 0 and os.path.isfile(linkpath):
        os.link(linkpath, dfile)
        pkg.log(f"using known distfile '{fname}'")

def invoke(pkg):
    srcdir = os.path.join(paths.sources(), f"{pkg.pkgname}-{pkg.version}")
    dfcount = 0
    dfgood = 0
    errors = 0

    if not os.path.isdir(srcdir):
        try:
            os.makedirs(srcdir)
            os.chown(srcdir, -1, os.getgid(), srcdir)
        except:
            pass

    if not os.path.isdir(srcdir):
        pkg.error(f"'{srcdir}' is not a directory")

    if len(pkg.distfiles) != len(pkg.checksum):
        pkg.error(f"checksums do not match distfiles")

    for dc in zip(pkg.distfiles, pkg.checksum):
        d, ck = dc
        if isinstance(d, tuple):
            fname = d[1]
            url = d[0]
        else:
            fname = d[d.rfind("/") + 1:]
            url = d
        dfile = os.path.join(srcdir, fname)
        if os.path.isfile(dfile):
            filesum = get_cksum(fname, dfile, pkg)
            if ck == filesum:
                dfgood += 1
            else:
                ino = os.stat(dfile).st_ino
                pkg.log_warn(f"wrong checksum found for {fname} - purging")
                # TODO

    if len(pkg.distfiles) == dfgood:
        return

    for dc in zip(pkg.distfiles, pkg.checksum):
        d, ck = dc
        if isinstance(d, tuple):
            fname = d[1]
            url = d[0]
        else:
            fname = d[d.rfind("/") + 1:]
            url = d
        dfile = os.path.join(srcdir, fname)
        if not os.path.isfile(dfile):
            link_cksum(fname, dfile, ck, pkg)
        if not os.path.isfile(dfile):
            pkg.log(f"fetching distfile '{fname}'...")
            try:
                fname = request.urlretrieve(url, dfile)
            except:
                pass
        if not os.path.isfile(dfile):
            pkg.error(f"failed to fetch '{fname}'")
        if not verify_cksum(fname, dfile, ck, pkg):
            errors += 1

    if errors > 0:
        pkg.error(f"couldn't verify distfiles")
