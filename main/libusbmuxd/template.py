pkgname = "libusbmuxd"
pkgver = "2.0.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libusb-devel", "libplist-devel"]
pkgdesc = "Client library to multiplex connections to/from iOS devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = (
    f"https://github.com/libimobiledevice/libusbmuxd/archive/{pkgver}.tar.gz"
)
sha256 = "8ae3e1d9340177f8f3a785be276435869363de79f491d05d8a84a59efc8a8fdc"
hardening = ["vis", "cfi"]


@subpackage("libusbmuxd-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libusbmuxd-progs")
def _progs(self):
    return self.default_progs()
