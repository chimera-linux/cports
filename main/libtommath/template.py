pkgname = "libtommath"
pkgver = "1.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TESTING=ON",
    "-DENABLE_CCACHE=OFF",  # automatic
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Portable number theoretic multiple-precision integer library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://www.libtom.net/LibTomMath"
source = f"https://github.com/libtom/libtommath/releases/download/v{pkgver}/ltm-{pkgver}.tar.xz"
sha256 = "296272d93435991308eb73607600c034b558807a07e829e751142e65ccfa9d08"


@subpackage("libtommath-devel")
def _(self):
    return self.default_devel()
