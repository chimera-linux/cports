pkgname = "taglib"
pkgver = "2.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["cppunit-devel", "utfcpp", "zlib-ng-compat-devel"]
pkgdesc = "Library for accessing ID tags in various media files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://taglib.github.io"
source = f"https://github.com/taglib/taglib/archive/v{pkgver}.tar.gz"
sha256 = "0de288d7fe34ba133199fd8512f19cc1100196826eafcb67a33b224ec3a59737"
hardening = ["!vis", "!cfi"]


@subpackage("taglib-devel")
def _(self):
    self.depends += ["zlib-ng-compat-devel"]

    return self.default_devel()
