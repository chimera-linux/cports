pkgname = "libusb"
pkgver = "1.0.24"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["eudev-devel", "linux-headers"]
pkgdesc = "Library for userspace USB device access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libusb.info"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "7efd2685f7b327326dcfb85cee426d9b871fd70e22caa15bb68d595ce2a2b12a"
options = ["lto"]

@subpackage("libusb-static")
def _static(self):
    return self.default_static()

@subpackage("libusb-devel")
def _devel(self):
    self.depends = ["eudev-devel"]
    return self.default_devel()
