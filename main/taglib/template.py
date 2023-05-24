pkgname = "taglib"
pkgver = "1.13"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DWITH_MP4=ON", "-DWITH_ASF=ON", "-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Library for accessing ID tags in various media files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://taglib.github.io"
source = f"https://github.com/{pkgname}/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "58f08b4db3dc31ed152c04896ee9172d22052bc7ef12888028c01d8b1d60ade0"
hardening = ["!cfi"]  # TODO
# test target does not work with shared libs
options = ["!check"]


@subpackage("taglib-devel")
def _devel(self):
    self.depends += ["zlib-devel"]

    return self.default_devel()
