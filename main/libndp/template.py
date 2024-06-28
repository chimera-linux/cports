pkgname = "libndp"
pkgver = "1.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Library for Neighbor Discovery Protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libndp.org"
source = f"{url}/files/{pkgname}-{pkgver}.tar.gz"
sha256 = "a8ab214e01dc3a9b615276905395637f391298c84d77651f0cbf0b1082dd2dd4"
# FIXME cfi
hardening = ["vis", "!cfi"]


@subpackage("libndp-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libndp-progs")
def _progs(self):
    return self.default_progs()
