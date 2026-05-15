pkgname = "python-gpgmepy"
pkgver = "2.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "automake",
    "libtool",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "swig",
]
makedepends = ["gpgme-devel", "libgpg-error-devel", "python-devel"]
renames = ["gpgme-python"]
pkgdesc = "Python bindings for gpgme"
license = "GPL-2.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/gpgmepy/gpgmepy-{pkgver}.tar.bz2"
sha256 = "07e1265648ff51da238c9af7a18b3f1dc7b0c66b4f21a72f27c74b396cd3336d"


def configure(self):
    self.do("autoreconf", "-if")
    self.do("./configure")
    self.mv("src", "gpg")


def check(self):
    libn = list((self.cwd / "build").glob("lib.*"))[0].name
    self.do(
        "make",
        "-C",
        "tests",
        "check",
        env={
            "TESTFLAGS": f"--python-libdir={self.chroot_cwd / 'build' / libn}"
        },
    )
