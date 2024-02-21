pkgname = "tslib"
pkgver = "1.23"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Touchscreen access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libts/tslib"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "9b489a54d48006201f2fe955a88c3f857535ac93b6cf8e5a16c7b166c8991dac"


@subpackage("tslib-progs")
def _progs(self):
    return self.default_progs()


@subpackage("tslib-devel")
def _devel(self):
    return self.default_devel()
