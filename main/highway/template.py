pkgname = "highway"
pkgver = "1.4.0"
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
license = "Apache-2.0 OR BSD-3-Clause"
url = "https://github.com/google/highway"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e72241ac9524bb653ae52ced768b508045d4438726a303f10181a38f764a453c"
# CFI: breaks a few tests
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("highway-devel")
def _(self):
    return self.default_devel()
