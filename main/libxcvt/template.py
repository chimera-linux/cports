pkgname = "libxcvt"
pkgver = "0.1.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Library to handle VESA CVT modeline generation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xkbcommon.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.xz"
sha256 = "27ebce180d355f94c1992930bedb40a36f6d7312ee50bf7f0acbcd22f33e8c29"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxcvt-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libxcvt-progs")
def _progs(self):
    return self.default_progs()
