pkgname = "intel-gmmlib"
pkgver = "22.8.1"
pkgrel = 0
# aarch64 segfaults in tests
# only needed for intel-media-driver anyway
archs = ["x86_64"]
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Intel Graphics Memory Management Library"
license = "MIT"
url = "https://github.com/intel/gmmlib"
source = f"{url}/archive/refs/tags/intel-gmmlib-{pkgver}.tar.gz"
sha256 = "9b8eac1891650021ded26b72585e7a2c702a3ba47565c968feabd14ab38d18f7"
# CFI: testsuite sigill
hardening = ["vis", "!cfi"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _(self):
    return self.default_devel()
