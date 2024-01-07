pkgname = "exiv2"
pkgver = "0.28.1"
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
url = "https://www.exiv2.org"
source = f"https://github.com/Exiv2/exiv2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3078651f995cb6313b1041f07f4dd1bf0e9e4d394d6e2adc6e92ad0b621291fa"
# needs gtest
options = ["!check"]


@subpackage("exiv2-devel")
def _devel(self):
    return self.default_devel()
