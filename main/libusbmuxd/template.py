pkgname = "libusbmuxd"
pkgver = "2.1.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "libimobiledevice-glue-devel",
    "libplist-devel",
    "libusb-devel",
]
pkgdesc = "Client library to multiplex connections to/from iOS devices"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libusbmuxd/releases/download/{pkgver}/libusbmuxd-{pkgver}.tar.bz2"
sha256 = "5546f1aba1c3d1812c2b47d976312d00547d1044b84b6a461323c621f396efce"


@subpackage("libusbmuxd-devel")
def _(self):
    return self.default_devel()


@subpackage("libusbmuxd-progs")
def _(self):
    return self.default_progs()
