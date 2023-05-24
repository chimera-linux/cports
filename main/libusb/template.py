pkgname = "libusb"
pkgver = "1.0.26"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
pkgdesc = "Library for userspace USB device access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libusb.info"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "12ce7a61fc9854d1d2a1ffe095f7b5fac19ddba095c259e6067a46500381b5a5"


@subpackage("libusb-devel")
def _devel(self):
    self.depends = ["virtual:pc:libudev!udev-devel"]
    return self.default_devel()


configure_gen = []
