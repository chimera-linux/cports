pkgname = "taglib"
pkgver = "2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["cppunit-devel", "utfcpp", "zlib-devel"]
pkgdesc = "Library for accessing ID tags in various media files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://taglib.github.io"
source = f"https://github.com/taglib/taglib/archive/v{pkgver}.tar.gz"
sha256 = "e36ea877a6370810b97d84cf8f72b1e4ed205149ab3ac8232d44c850f38a2859"
hardening = ["!cfi"]  # TODO


@subpackage("taglib-devel")
def _devel(self):
    self.depends += ["zlib-devel"]

    return self.default_devel()
