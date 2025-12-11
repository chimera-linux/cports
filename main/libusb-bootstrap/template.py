pkgname = "libusb-bootstrap"
pkgver = "1.0.29"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static", "--disable-udev"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
depends = ["!libusb", "!libusb-devel"]
provides = ["so:libusb-1.0.so.0=0", "pc:libusb-1.0=0"]
pkgdesc = "Bootstrap version of libusb"
license = "LGPL-2.1-or-later"
url = "https://libusb.info"
source = f"https://github.com/libusb/libusb/releases/download/v{pkgver}/libusb-{pkgver}.tar.bz2"
sha256 = "5977fc950f8d1395ccea9bd48c06b3f808fd3c2c961b44b0c2e6e29fc3a70a85"
# check is pointless here
options = ["!check", "!scanshlibs", "!scanpkgconf"]
