pkgname = "taglib"
pkgver = "2.3.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["cppunit-devel", "utfcpp", "zlib-ng-compat-devel"]
pkgdesc = "Library for accessing ID tags in various media files"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://taglib.github.io"
source = f"https://github.com/taglib/taglib/archive/v{pkgver}.tar.gz"
sha256 = "cda2d6dac7f12a84e46fbb0907bb1a1ec0679e4722b5237576be5563e295244e"
hardening = ["!vis", "!cfi"]


@subpackage("taglib-devel")
def _(self):
    self.depends += ["zlib-ng-compat-devel"]

    return self.default_devel()
