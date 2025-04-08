pkgname = "libusb"
pkgver = "1.0.28"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["udev-devel", "linux-headers"]
pkgdesc = "Library for userspace USB device access"
license = "LGPL-2.1-or-later"
url = "https://libusb.info"
source = f"https://github.com/libusb/libusb/releases/download/v{pkgver}/libusb-{pkgver}.tar.bz2"
sha256 = "966bb0d231f94a474eaae2e67da5ec844d3527a1f386456394ff432580634b29"


@subpackage("libusb-devel")
def _(self):
    self.depends = ["pc:libudev!udev-devel"]
    return self.default_devel()
