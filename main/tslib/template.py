pkgname = "tslib"
pkgver = "1.24"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Touchscreen access library"
license = "LGPL-2.1-or-later"
url = "https://github.com/libts/tslib"
source = f"{url}/releases/download/{pkgver}/tslib-{pkgver}.tar.xz"
sha256 = "58d9941ffaa269c399f00d0d308184c96087f7acf69aa8e3c6645e852f993ba2"
options = ["etcfiles"]


@subpackage("tslib-progs")
def _(self):
    return self.default_progs()


@subpackage("tslib-devel")
def _(self):
    return self.default_devel()
