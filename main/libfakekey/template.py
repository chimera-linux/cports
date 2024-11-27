pkgname = "libfakekey"
pkgver = "0.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["libxtst-devel"]
pkgdesc = "Library for simulating X11 keypresses"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://git.yoctoproject.org/libfakekey"
source = f"http://git.yoctoproject.org/cgit/cgit.cgi/libfakekey/snapshot/libfakekey-{pkgver}.tar.gz"
sha256 = "d282fa6481a5b85f71e36e8bad4cfa938cc8eaac4c42ffa27f9203ac634813f4"


@subpackage("libfakekey-devel")
def _(self):
    return self.default_devel()
