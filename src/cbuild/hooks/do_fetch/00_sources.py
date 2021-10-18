from cbuild.core import paths
import os
import hashlib
from urllib import request

sites = {
    "sourceforge": "https://downloads.sourceforge.net/sourceforge",
    "freedesktop": "https://freedesktop.org/software",
    "mozilla": "https://ftp.mozilla.org/pub",
    "debian": "http://ftp.debian.org/debian/pool",
    "ubuntu": "http://archive.ubuntu.com/ubuntu/pool",
    "nongnu": "https://download.savannah.nongnu.org/releases",
    "kernel": "https://www.kernel.org/pub/linux",
    "gnome": "https://download.gnome.org/sources",
    "xorg": "https://www.x.org/releases/individual",
    "cpan": "https://www.cpan.org/modules/by-module",
    "pypi": "https://files.pythonhosted.org/packages/source",
    "gnu": "https://ftp.gnu.org/gnu",
    "kde": "https://download.kde.org/stable",
}

def get_cksum(fname, dfile, pkg):
    return hashlib.sha256(dfile.read_bytes()).hexdigest()

def verify_cksum(fname, dfile, cksum, pkg):
    pkg.log(f"verifying sha256sums for source '{fname}'... ", "")
    filesum = get_cksum(fname, dfile, pkg)
    if cksum != filesum:
        pkg.logger.out_plain("")
        pkg.logger.out_red(f"SHA256 mismatch for '{fname}':\n{filesum}")
        return False
    else:
        shapath = paths.sources() / "by_sha256"
        linkpath = shapath / f"{cksum}_{fname}"
        if not linkpath.is_file():
            shapath.mkdir(parents = True, exist_ok = True)
            dfile.link_to(linkpath)
        pkg.logger.out_plain("OK.")
        return True

def link_cksum(fname, dfile, cksum, pkg):
    shapath = paths.sources() / "by_sha256"
    linkpath = shapath / f"{cksum}_{fname}"
    if len(cksum) > 0 and linkpath.is_file():
        linkpath.link_to(dfile)
        pkg.log(f"using known source '{fname}'")

def interp_url(pkg, url):
    if not url.startswith("$("):
        return url

    import re

    def matchf(m):
        mw = m.group(1).removesuffix("_SITE").lower()
        if not mw in sites:
            pkg.error(f"malformed source URL '{url}'")
        return sites[mw]

    return re.sub(r"\$\((\w+)\)", matchf, url)

def get_nameurl(pkg, d):
    if isinstance(d, tuple):
        if not isinstance(d[1], bool):
            return interp_url(pkg, d[0]), d[1]
        else:
            return interp_url(pkg, d[0]), d[0][d[0].rfind("/") + 1:]

    return interp_url(pkg, d), d[d.rfind("/") + 1:]

def invoke(pkg):
    srcdir = paths.sources() / f"{pkg.pkgname}-{pkg.pkgver}"
    dfcount = 0
    dfgood = 0
    errors = 0

    if not srcdir.is_dir():
        try:
            srcdir.mkdir(parents = True)
            os.chown(srcdir, -1, os.getgid(), srcdir)
        except:
            pass

    if not srcdir.is_dir():
        pkg.error(f"'{srcdir}' is not a directory")

    if len(pkg.source) != len(pkg.sha256):
        pkg.error(f"sha256sums do not match sources")

    for dc in zip(pkg.source, pkg.sha256):
        d, ck = dc
        url, fname = get_nameurl(pkg, d)
        dfile = srcdir / fname
        if dfile.is_file():
            filesum = get_cksum(fname, dfile, pkg)
            if ck == filesum:
                dfgood += 1
            else:
                ino = dfile.stat().st_ino
                pkg.log_warn(f"wrong sha256 found for {fname} - purging")
                # TODO

    if len(pkg.source) == dfgood:
        return

    for dc in zip(pkg.source, pkg.sha256):
        d, ck = dc
        url, fname = get_nameurl(pkg, d)
        dfile = srcdir / fname
        if not dfile.is_file():
            link_cksum(fname, dfile, ck, pkg)
        if not dfile.is_file():
            pkg.log(f"fetching source '{fname}'...")
            try:
                fname = request.urlretrieve(url, str(dfile))[0]
                fname = os.path.basename(fname)
            except Exception as e:
                pkg.log_warn(f"error fetching '{fname}': {e}")
        if not dfile.is_file():
            pkg.error(f"failed to fetch '{fname}'")
        if not verify_cksum(fname, dfile, ck, pkg):
            errors += 1

    if errors > 0:
        pkg.error(f"couldn't verify sources")
