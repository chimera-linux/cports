pkgname = "usbutils"
pkgver = "019"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["udev-devel", "libusb-devel", "linux-headers"]
depends = ["hwdata-usb"]
pkgdesc = "Linux USB utilities"
license = "GPL-2.0-only"
url = "http://linux-usb.sourceforge.net"
source = f"$(KERNEL_SITE)/utils/usb/usbutils/usbutils-{pkgver}.tar.xz"
sha256 = "659f40c440e31ba865c52c818a33d3ba6a97349e3353f8b1985179cb2aa71ec5"
hardening = ["vis", "cfi"]


def post_install(self):
    self.uninstall("usr/bin/lsusb.py")
