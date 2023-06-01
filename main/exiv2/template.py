pkgname = "exiv2"
pkgver = "0.28.0"
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
source = f"https://github.com/Exiv2/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}-Source.tar.gz"
sha256 = "89af3b5ef7277753ef7a7b5374ae017c6b9e304db3b688f1948e73e103491f3d"
# needs gtest
options = ["!check"]


@subpackage("exiv2-devel")
def _devel(self):
    return self.default_devel()
