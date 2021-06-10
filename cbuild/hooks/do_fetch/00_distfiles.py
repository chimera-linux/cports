from cbuild.core import paths
import os
import hashlib
from urllib import request

def get_cksum(fname, dfile, pkg):
    return hashlib.sha256(dfile.read_bytes()).hexdigest()

def verify_cksum(fname, dfile, cksum, pkg):
    pkg.log(f"verifying checksum for distfile '{fname}'... ", "")
    filesum = get_cksum(fname, dfile, pkg)
    if cksum != filesum:
        pkg.logger.out_plain("")
        pkg.logger.out_red(f"SHA256 mismatch for '{fname}':\n@{filesum}")
        return False
    else:
        shapath = paths.sources() / "by_sha256"
        linkpath = shapath / f"{cksum}_{fname}"
        if not linkpath.is_file():
            os.makedirs(shapath, exist_ok = True)
            dfile.link_to(linkpath)
        pkg.logger.out_plain("OK.")

def link_cksum(fname, dfile, cksum, pkg):
    shapath = paths.sources() / "by_sha256"
    linkpath = shapath / f"{cksum}_{fname}"
    if len(cksum) > 0 and linkpath.is_file():
        dfile.link_to(linkpath)
        pkg.log(f"using known distfile '{fname}'")

def invoke(pkg):
    srcdir = paths.sources() / f"{pkg.pkgname}-{pkg.version}"
    dfcount = 0
    dfgood = 0
    errors = 0

    if not srcdir.is_dir():
        try:
            os.makedirs(srcdir)
            os.chown(srcdir, -1, os.getgid(), srcdir)
        except:
            pass

    if not srcdir.is_dir():
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
        dfile = srcdir / fname
        if dfile.is_file():
            filesum = get_cksum(fname, dfile, pkg)
            if ck == filesum:
                dfgood += 1
            else:
                ino = dfile.stat().st_ino
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
        dfile = srcdir / fname
        if not dfile.is_file():
            link_cksum(fname, dfile, ck, pkg)
        if not dfile.is_file():
            pkg.log(f"fetching distfile '{fname}'...")
            try:
                fname = request.urlretrieve(url, str(dfile))[0]
                fname = os.path.basename(fname)
            except:
                pass
        if not dfile.is_file():
            pkg.error(f"failed to fetch '{fname}'")
        if not verify_cksum(fname, dfile, ck, pkg):
            errors += 1

    if errors > 0:
        pkg.error(f"couldn't verify distfiles")
