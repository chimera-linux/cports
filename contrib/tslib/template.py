pkgname = "tslib"
pkgver = "1.22"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Touchscreen access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libts/tslib"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "aaf0aed410a268d7b51385d07fe4d9d64312038e87c447ec8a24c8db0a15617a"

@subpackage("tslib-progs")
def _progs(self):
    return self.default_progs()

@subpackage("tslib-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
