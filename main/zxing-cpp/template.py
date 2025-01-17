pkgname = "zxing-cpp"
pkgver = "2.3.0"
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
sha256 = "64e4139103fdbc57752698ee15b5f0b0f7af9a0331ecbdc492047e0772c417ba"


@subpackage("zxing-cpp-devel")
def _(self):
    return self.default_devel()
