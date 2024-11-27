pkgname = "libebml"
pkgver = "1.4.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "C++ library to parse Extensible Binary Meta-Language files"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://matroska-org.github.io/libebml"
source = f"https://dl.matroska.org/downloads/libebml/libebml-{pkgver}.tar.xz"
sha256 = "4971640b0592da29c2d426f303e137a9b0b3d07e1b81d069c1e56a2f49ab221b"


@subpackage("libebml-devel")
def _(self):
    return self.default_devel()
