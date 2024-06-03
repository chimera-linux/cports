pkgname = "ivykis"
pkgver = "0.43.1"
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
sha256 = "c7d2b18bd9342e7edfd13e0e38a68dbfeaa6d31e92e3e6772baa39429dfebb9f"


@subpackage("ivykis-devel")
def _devel(self):
    return self.default_devel()
