pkgname = "librtas"
pkgver = "2.0.2"
pkgrel = 0
archs = ["ppc*"]
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Librtas library for Linux on Power systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibm-power-utilities/librtas"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b47b2a6f140347ac265e2c66ddf68293f6cdcc7c0c9a78c6e21ff52846465415"

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

@subpackage("librtas-static")
def _static(self):
    return self.default_static()

@subpackage("librtas-devel")
def _devel(self):
    return self.default_devel()
