pkgname = "ivykis"
pkgver = "0.42.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for asynchronous I/O readiness notification"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "http://libivykis.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/libivykis/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6ef8ed255814e5068473356877da55d67493eeafd978884cdecc5a3e58067129"

@subpackage("ivykis-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
