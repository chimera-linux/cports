pkgname = "highway"
pkgver = "1.0.7"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DHWY_SYSTEM_GTEST=ON",
    "-DHWY_ENABLE_EXAMPLES=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "Google's SIMD library with runtime dispatch"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR BSD-3-Clause"
url = "https://github.com/google/highway"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5434488108186c170a5e2fca5e3c9b6ef59a1caa4d520b008a9b8be6b8abe6c5"
# FIXME: cfi breaks a few tests
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE-BSD3")


@subpackage("highway-devel")
def _devel(self):
    return self.default_devel()
