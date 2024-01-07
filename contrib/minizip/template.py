pkgname = "minizip"
pkgver = "1.3"
pkgrel = 0
build_wrksrc = "contrib/minizip"
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Zip file manipulation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://www.winimage.com/zLibDll/minizip.html"
source = f"https://www.zlib.net/fossils/zlib-{pkgver}.tar.gz"
sha256 = "ff0ba4c292013dbc27530b3a81e1f9a813cd39de01ca5e0f8bf355702efa593e"


def post_install(self):
    self.rm(self.destdir / "usr/include/minizip/crypt.h")


@subpackage("minizip-devel")
def _devel(self):
    return self.default_devel()
