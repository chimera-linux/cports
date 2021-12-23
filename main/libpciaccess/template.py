pkgname = "libpciaccess"
pkgver = "0.16"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "X11 PCI access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.bz2"
sha256 = "214c9d0d884fdd7375ec8da8dcb91a8d3169f263294c9a90c575bf1938b9f489"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libpciaccess-static")
def _static(self):
    return self.default_static()

@subpackage("libpciaccess-devel")
def _devel(self):
    return self.default_devel()
