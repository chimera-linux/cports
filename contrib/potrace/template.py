pkgname = "potrace"
pkgver = "1.16"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-libpotrace"]
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Bitmap to vector tracer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://potrace.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "be8248a17dedd6ccbaab2fcc45835bb0502d062e40fbded3bc56028ce5eb7acc"


@subpackage("potrace-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
