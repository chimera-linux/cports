pkgname = "libusb"
pkgver = "1.0.29"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
pkgdesc = "Library for userspace USB device access"
license = "LGPL-2.1-or-later"
url = "https://libusb.info"
source = f"https://github.com/libusb/libusb/releases/download/v{pkgver}/libusb-{pkgver}.tar.bz2"
sha256 = "5977fc950f8d1395ccea9bd48c06b3f808fd3c2c961b44b0c2e6e29fc3a70a85"


@subpackage("libusb-devel")
def _(self):
    self.depends = ["pc:libudev!udev-devel"]
    return self.default_devel()
