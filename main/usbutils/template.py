pkgname = "usbutils"
pkgver = "018"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["udev-devel", "libusb-devel", "linux-headers"]
depends = ["hwdata-usb"]
pkgdesc = "Linux USB utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://linux-usb.sourceforge.net"
source = f"$(KERNEL_SITE)/utils/usb/usbutils/usbutils-{pkgver}.tar.xz"
sha256 = "83f68b59b58547589c00266e82671864627593ab4362d8c807f50eea923cad93"
hardening = ["vis", "cfi"]


def post_install(self):
    self.uninstall("usr/bin/lsusb.py")
