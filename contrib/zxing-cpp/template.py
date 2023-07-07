pkgname = "zxing-cpp"
pkgver = "2.1.0"
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
sha256 = "6d54e403592ec7a143791c6526c1baafddf4c0897bb49b1af72b70a0f0c4a3fe"


@subpackage("zxing-cpp-devel")
def _devel(self):
    return self.default_devel()
