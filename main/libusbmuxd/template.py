pkgname = "libusbmuxd"
pkgver = "2.1.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "libimobiledevice-glue-devel",
    "libplist-devel",
    "libusb-devel",
]
pkgdesc = "Client library to multiplex connections to/from iOS devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libusbmuxd/releases/download/{pkgver}/libusbmuxd-{pkgver}.tar.bz2"
sha256 = "c35bf68f8e248434957bd5b234c389b02206a06ecd9303a7fb931ed7a5636b16"
patch_style = "patch"
hardening = ["vis", "cfi"]


@subpackage("libusbmuxd-devel")
def _(self):
    return self.default_devel()


@subpackage("libusbmuxd-progs")
def _(self):
    return self.default_progs()
