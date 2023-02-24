pkgname = "usbutils"
pkgver = "014"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["udev-devel", "libusb-devel", "linux-headers"]
depends = ["hwdata-usb"]
pkgdesc = "Linux USB utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://linux-usb.sourceforge.net"
source = f"$(KERNEL_SITE)/utils/usb/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3a079cfad60560227b67192482d7813bf96326fcbb66c04254839715f276fc69"
hardening = ["vis", "cfi"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.rm(self.destdir / "usr/bin/lsusb.py")
