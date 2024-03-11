pkgname = "ivykis"
pkgver = "0.43"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for asynchronous I/O readiness notification"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "http://libivykis.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/libivykis/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ff1c09569a806f2e926c8f9545fbf70d10f6fe14b66e2077e7dab1ca8e52a269"


@subpackage("ivykis-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
