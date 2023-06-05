pkgname = "zxing-cpp"
pkgver = "2.0.0"
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
sha256 = "12b76b7005c30d34265fc20356d340da179b0b4d43d2c1b35bcca86776069f76"


@subpackage("zxing-cpp-devel")
def _devel(self):
    return self.default_devel()
