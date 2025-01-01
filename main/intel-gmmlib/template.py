pkgname = "intel-gmmlib"
pkgver = "22.6.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/intel/gmmlib"
source = f"{url}/archive/refs/tags/intel-gmmlib-{pkgver}.tar.gz"
sha256 = "2be3de25e45ed6b32d6ea173510b9e4ce141c22f9d6ed18dd5b574b33f34748c"
# CFI: testsuite sigill
hardening = ["vis", "!cfi"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _(self):
    return self.default_devel()
