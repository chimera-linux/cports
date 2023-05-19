pkgname = "librtas"
pkgver = "2.0.4"
pkgrel = 0
archs = ["ppc*"]
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Librtas library for Linux on Power systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibm-power-utilities/librtas"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8a27d97fa2929441ac607225f522267361d2dd26dd3858d6ba2869af2eb50d27"

@subpackage("librtas-devel")
def _devel(self):
    return self.default_devel()
