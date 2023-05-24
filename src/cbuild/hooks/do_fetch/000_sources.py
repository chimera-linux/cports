from cbuild.core import paths

import os
import hashlib
from urllib import request


def get_cksum(dfile, pkg):
    return hashlib.sha256(dfile.read_bytes()).hexdigest()


def make_link(dfile, cksum):
    shapath = paths.sources() / "by_sha256"
    linkpath = shapath / f"{cksum}_{dfile.name}"
    if not linkpath.is_file():
        shapath.mkdir(parents=True, exist_ok=True)
        dfile.link_to(linkpath)
    else:
        tino = linkpath.stat().st_ino
        sino = dfile.stat().st_ino
        # if inodes differ, make sure to sync it
        if tino != sino:
            linkpath.unlink()
            dfile.link_to(linkpath)


def verify_cksum(dfile, cksum, pkg):
    pkg.log(f"verifying sha256sums for source '{dfile.name}'... ", "")
    filesum = get_cksum(dfile, pkg)
    if cksum != filesum:
        pkg.logger.out_plain("")
        pkg.logger.out_red(f"SHA256 mismatch for '{dfile.name}':\n{filesum}")
        return False
    else:
        make_link(dfile, cksum)
        pkg.logger.out_plain("OK.")
        return True


def link_cksum(dfile, cksum, pkg):
    shapath = paths.sources() / "by_sha256"
    linkpath = shapath / f"{cksum}_{dfile.name}"
    if len(cksum) > 0 and linkpath.is_file():
        linkpath.link_to(dfile)
        pkg.log(f"using known source '{dfile.name}'")


def get_nameurl(d):
    if isinstance(d, tuple):
        if not isinstance(d[1], bool):
            return d[0], d[1]
        else:
            return d[0], d[0][d[0].rfind("/") + 1 :]

    return d, d[d.rfind("/") + 1 :]


def invoke(pkg):
    srcdir = paths.sources() / f"{pkg.pkgname}-{pkg.pkgver}"

    dfgood = 0
    errors = 0

    if len(pkg.source) != len(pkg.sha256):
        pkg.error("sha256sums do not match sources")

    if not srcdir.is_dir():
        try:
            srcdir.mkdir(parents=True)
            os.chown(srcdir, -1, os.getgid(), srcdir)
        except Exception:
            pass

    if not srcdir.is_dir():
        pkg.error(f"'{srcdir}' is not a directory")

    for dc in zip(pkg.source, pkg.sha256):
        d, ck = dc
        url, fname = get_nameurl(d)
        dfile = srcdir / fname
        if dfile.is_file():
            filesum = get_cksum(dfile, pkg)
            if ck == filesum:
                make_link(dfile, filesum)
                dfgood += 1
            else:
                pkg.log_warn(f"wrong sha256 found for {fname} - purging")
                dfile.unlink()

    if len(pkg.source) == dfgood:
        return

    for dc in zip(pkg.source, pkg.sha256):
        d, ck = dc
        url, fname = get_nameurl(d)
        dfile = srcdir / fname
        if not dfile.is_file():
            link_cksum(dfile, ck, pkg)
        if not dfile.is_file():
            pkg.log(f"fetching source '{fname}'...")
            try:
                rq = request.Request(
                    url,
                    data=None,
                    headers={
                        "User-Agent": "cbuild-fetch/4.20.69",
                        "Accept": "*/*",
                    },
                )
                rqf = request.urlopen(rq)
                with open(dfile, "wb") as df:
                    df.write(rqf.read())
            except Exception as e:
                pkg.log_warn(f"error fetching '{dfile.name}': {e}")
        if not dfile.is_file():
            pkg.error(f"failed to fetch '{dfile.name}'")
        if not verify_cksum(dfile, ck, pkg):
            errors += 1

    if errors > 0:
        pkg.error("couldn't verify sources")
