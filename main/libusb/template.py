pkgname = "libusb"
pkgver = "1.0.25"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["eudev-devel", "linux-headers"]
pkgdesc = "Library for userspace USB device access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libusb.info"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "8a28ef197a797ebac2702f095e81975e2b02b2eeff2774fa909c78a74ef50849"

@subpackage("libusb-devel")
def _devel(self):
    self.depends = ["eudev-devel"]
    return self.default_devel()
