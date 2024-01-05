pkgname = "usbutils"
pkgver = "017"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["automake", "libtool", "pkgconf", "gmake"]
makedepends = ["udev-devel", "libusb-devel", "linux-headers"]
depends = ["hwdata-usb"]
pkgdesc = "Linux USB utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://linux-usb.sourceforge.net"
source = f"$(KERNEL_SITE)/utils/usb/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a6a25ffdcf9103e38d7a44732aca17073f4e602b92e4ae55625231a82702e05b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/bin/lsusb.py")
    self.rm(self.destdir / "usr/lib/pkgconfig", recursive=True)
