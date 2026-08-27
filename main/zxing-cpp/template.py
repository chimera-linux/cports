pkgname = "zxing-cpp"
pkgver = "3.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DZXING_UNIT_TESTS=ON",
    "-DZXING_BLACKBOX_TESTS=OFF",
    "-DZXING_EXAMPLES=ON",
    "-DZXING_DEPENDENCIES=LOCAL",
    "-DZXING_WRITERS=BOTH",
]
# racey
make_check_args = ["-j1"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["gtest-devel", "stb"]
pkgdesc = "Multi-format 1D/2D barcode library"
license = "Apache-2.0"
url = "https://github.com/nu-book/zxing-cpp"
source = f"{url}/releases/download/v{pkgver}/zxing-cpp-{pkgver}.tar.gz"
sha256 = "c3c02c29c0b519de7bd4e25b376e606e87f0761befd1282815642a2246613d14"


@subpackage("zxing-cpp-devel")
def _(self):
    return self.default_devel()


@subpackage("zxing-cpp-progs")
def _(self):
    return self.default_progs()
