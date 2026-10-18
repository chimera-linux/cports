pkgname = "diffoscope"
pkgver = "334"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
depends = [
    "file",
    "llvm-binutils",
    "python",
    "python-libarchive-c",
    "python-magic",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "In-depth comparison of files, archives, and directories"
license = "GPL-3.0-or-later"
url = "https://diffoscope.org"
source = f"https://salsa.debian.org/reproducible-builds/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "ddf0605787f73ce29ebaa02c1f0df3a07bfb51bf5df882f8cf2b44594866bfc0"


def post_install(self):
    self.install_license("COPYING")
