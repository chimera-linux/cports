pkgname = "ivykis"
pkgver = "0.43.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Library for asynchronous I/O readiness notification"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "http://libivykis.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/libivykis/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "93e3e9b237695437cd63d4aa48a8d9dfd8b39bc28a192a5770d113c4fe9099ef"


@subpackage("ivykis-devel")
def _devel(self):
    return self.default_devel()
