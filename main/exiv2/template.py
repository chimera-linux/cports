pkgname = "exiv2"
pkgver = "0.28.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DEXIV2_BUILD_SAMPLES=OFF",
    "-DEXIV2_ENABLE_BMFF=ON",
    "-DEXIV2_BUILD_UNIT_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = [
    "brotli-devel",
    "gtest-devel",
    "inih-devel",
    "libexpat-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Image metadata manipulation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://exiv2.org"
source = f"https://github.com/Exiv2/exiv2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "65cb3a813f34fb6db7a72bba3fc295dd6c419082d2d8bbf96518be6d1024b784"


@subpackage("exiv2-devel")
def _(self):
    return self.default_devel()
