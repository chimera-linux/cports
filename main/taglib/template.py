pkgname = "taglib"
pkgver = "1.13.1"
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
sha256 = "c8da2b10f1bfec2cd7dbfcd33f4a2338db0765d851a50583d410bacf055cfd0b"
hardening = ["!cfi"]  # TODO
# test target does not work with shared libs
options = ["!check"]


@subpackage("taglib-devel")
def _devel(self):
    self.depends += ["zlib-devel"]

    return self.default_devel()
