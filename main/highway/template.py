pkgname = "highway"
pkgver = "1.1.0"
pkgrel = 0
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
makedepends = ["gtest-devel", "linux-headers"]
pkgdesc = "Google's SIMD library with runtime dispatch"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR BSD-3-Clause"
url = "https://github.com/google/highway"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "354a8b4539b588e70b98ec70844273e3f2741302c4c377bcc4e81b3d1866f7c9"
# FIXME: cfi breaks a few tests
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE-BSD3")


@subpackage("highway-devel")
def _devel(self):
    return self.default_devel()
