pkgname = "intel-gmmlib"
pkgver = "22.3.9"
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
sha256 = "62d2f8333f1da3361952546a83dd40d1eb23d8bddacf67a160e63f565b68b5a6"
# FIXME: cfi testsuite sigill
hardening = ["vis"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _devel(self):
    return self.default_devel()
