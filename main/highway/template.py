pkgname = "highway"
pkgver = "1.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DHWY_CMAKE_RVV=OFF",
    "-DHWY_SYSTEM_GTEST=ON",
    "-DHWY_ENABLE_EXAMPLES=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel", "linux-headers"]
pkgdesc = "Google's SIMD library with runtime dispatch"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR BSD-3-Clause"
url = "https://github.com/google/highway"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7e0be78b8318e8bdbf6fa545d2ecb4c90f947df03f7aadc42c1967f019e63343"
# CFI: breaks a few tests
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE-BSD3")


@subpackage("highway-devel")
def _(self):
    return self.default_devel()
