pkgname = "libiio"
pkgver = "0.26"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DWITH_ZSTD=ON",
    "-DUDEV_RULES_INSTALL_DIR=/usr/lib/udev/rules.d",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "avahi-devel",
    "bison",
    "flex",
    "libaio-devel",
    "libusb-devel",
    "libxml2-devel",
    "linux-headers",
    "zstd-devel",
]
pkgdesc = "Library for interfacing with local and remote Linux IIO devices"
maintainer = "Anthony <w732qq@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/analogdevicesinc/libiio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fb445fb860ef1248759f45d4273a4eff360534480ec87af64c6b8db3b99be7e5"


@subpackage("libiio-devel")
def _(self):
    return self.default_devel()
