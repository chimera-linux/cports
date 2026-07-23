pkgname = "libusb"
pkgver = "1.0.30"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
pkgdesc = "Library for userspace USB device access"
license = "LGPL-2.1-or-later"
url = "https://libusb.info"
source = f"https://github.com/libusb/libusb/releases/download/v{pkgver}/libusb-{pkgver}.tar.bz2"
sha256 = "fea36f34f9156400209595e300840767ab1a385ede1dc7ee893015aea9c6dbaf"


@subpackage("libusb-devel")
def _(self):
    self.depends = ["pc:libudev!udev-devel"]
    return self.default_devel()
