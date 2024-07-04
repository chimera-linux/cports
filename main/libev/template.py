pkgname = "libev"
pkgver = "4.33"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "High-performance event loop loosely modelled after libevent"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause OR GPL-2.0-or-later"
url = "http://software.schmorp.de/pkg/libev.html"
source = f"http://dist.schmorp.de/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "507eb7b8d1015fbec5b935f34ebed15bf346bed04a11ab82b8eee848c4205aea"


def post_install(self):
    # conflicts with libevent, not necessary
    self.uninstall("usr/include/event.h")
    self.install_license("LICENSE")


@subpackage("libev-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
