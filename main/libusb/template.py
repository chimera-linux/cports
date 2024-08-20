pkgname = "libusb"
pkgver = "1.0.27"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
pkgdesc = "Library for userspace USB device access"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libusb.info"
source = f"https://github.com/libusb/libusb/releases/download/v{pkgver}/libusb-{pkgver}.tar.bz2"
sha256 = "ffaa41d741a8a3bee244ac8e54a72ea05bf2879663c098c82fc5757853441575"


@subpackage("libusb-devel")
def _(self):
    self.depends = ["pc:libudev!udev-devel"]
    return self.default_devel()
