pkgname = "intel-gmmlib"
pkgver = "22.4.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/intel/gmmlib"
source = f"https://github.com/intel/gmmlib/archive/refs/tags/intel-gmmlib-{pkgver}.tar.gz"
sha256 = "7233037c5788966b0b356823149247e4d3bd590480103c48277191da83243d0d"
# FIXME: cfi testsuite sigill
hardening = ["vis"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _devel(self):
    return self.default_devel()
