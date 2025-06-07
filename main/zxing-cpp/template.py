pkgname = "zxing-cpp"
pkgver = "2.3.0"
pkgrel = 3
build_style = "cmake"
configure_args = [
    "-DZXING_UNIT_TESTS=ON",
    "-DZXING_BLACKBOX_TESTS=OFF",
    "-DZXING_EXAMPLES=ON",
    "-DZXING_DEPENDENCIES=LOCAL",
]
# racey
make_check_args = ["-j1"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["gtest-devel", "stb"]
pkgdesc = "Multi-format 1D/2D barcode library"
license = "Apache-2.0"
url = "https://github.com/nu-book/zxing-cpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "64e4139103fdbc57752698ee15b5f0b0f7af9a0331ecbdc492047e0772c417ba"


@subpackage("zxing-cpp-devel")
def _(self):
    return self.default_devel()


@subpackage("zxing-cpp-progs")
def _(self):
    return self.default_progs()
