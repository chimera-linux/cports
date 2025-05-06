pkgname = "intel-gmmlib"
pkgver = "22.7.2"
pkgrel = 0
# aarch64 segfaults in tests
# only needed for intel-media-driver anyway
archs = ["x86_64"]
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Intel Graphics Memory Management Library"
license = "MIT"
url = "https://github.com/intel/gmmlib"
source = f"{url}/archive/refs/tags/intel-gmmlib-{pkgver}.tar.gz"
sha256 = "36f2ff2b59158d1253a33d735f4e35a1b5740c4751818bdaa222b8ddf96ee881"
# CFI: testsuite sigill
hardening = ["vis", "!cfi"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _(self):
    return self.default_devel()
