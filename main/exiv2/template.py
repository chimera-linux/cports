pkgname = "exiv2"
pkgver = "0.28.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DEXIV2_BUILD_SAMPLES=OFF",
    "-DEXIV2_ENABLE_BMFF=ON",
    "-DEXIV2_BUILD_UNIT_TESTS=OFF",
]
make_check_target = "unit_test"
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["libexpat-devel", "zlib-devel", "brotli-devel", "inih-devel"]
pkgdesc = "Image metadata manipulation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://exiv2.org"
source = f"https://github.com/Exiv2/exiv2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "543bead934135f20f438e0b6d8858c55c5fcb7ff80f5d1d55489965f1aad58b9"
# needs gtest
options = ["!check"]


@subpackage("exiv2-devel")
def _devel(self):
    return self.default_devel()
