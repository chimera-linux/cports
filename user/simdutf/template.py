pkgname = "simdutf"
pkgver = "9.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Library of SIMD-accelerated Unicode routines"
license = "MIT"
url = "https://github.com/simdutf/simdutf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fd2ce975f29809a975a8da8843cfb3a7265af3f71be548f199d23cf65e101764"


def post_install(self):
    self.install_license("LICENSE-MIT")


@subpackage("simdutf-devel")
def _(self):
    return self.default_devel()
