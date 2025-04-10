pkgname = "exiv2"
pkgver = "0.28.5"
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
license = "GPL-2.0-or-later"
url = "https://exiv2.org"
source = f"https://github.com/Exiv2/exiv2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e1671f744e379a87ba0c984617406fdf8c0ad0c594e5122f525b2fb7c28d394d"
# check may be disabled
options = []

if self.profile().wordsize == 32:
    # Tests fail with overflow in addition
    # https://github.com/Exiv2/exiv2/issues/2539
    options += ["!check"]


@subpackage("exiv2-devel")
def _(self):
    return self.default_devel()
