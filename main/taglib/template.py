pkgname = "taglib"
pkgver = "1.12"
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
sha256 = "b5a56f78a8bd962aaaec992b25a031f541b949b6eb30aa232bd6d5fa17cf8fa8"
# test target does not work with shared libs
options = ["!check"]

@subpackage("taglib-devel")
def _devel(self):
    self.depends += ["zlib-devel"]

    return self.default_devel()
