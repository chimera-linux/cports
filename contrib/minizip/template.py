pkgname = "minizip"
pkgver = "1.3.1"
pkgrel = 0
build_wrksrc = "contrib/minizip"
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Zip file manipulation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://www.winimage.com/zLibDll/minizip.html"
source = f"https://www.zlib.net/fossils/zlib-{pkgver}.tar.gz"
sha256 = "9a93b2b7dfdac77ceba5a558a580e74667dd6fede4585b91eefb60f03b72df23"


def post_install(self):
    self.uninstall("usr/include/minizip/crypt.h")


@subpackage("minizip-devel")
def _devel(self):
    return self.default_devel()
