pkgname = "zxing-cpp"
pkgver = "2.2.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_UNIT_TESTS=ON",
    "-DBUILD_EXAMPLES=OFF",
    "-DBUILD_BLACKBOX_TESTS=OFF",
    "-DBUILD_DEPENDENCIES=LOCAL",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
checkdepends = ["gtest-devel"]
pkgdesc = "Multi-format 1D/2D barcode library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/nu-book/zxing-cpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "02078ae15f19f9d423a441f205b1d1bee32349ddda7467e2c84e8f08876f8635"


@subpackage("zxing-cpp-devel")
def _(self):
    return self.default_devel()
