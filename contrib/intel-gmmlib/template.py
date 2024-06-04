pkgname = "intel-gmmlib"
pkgver = "22.3.20"
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
sha256 = "227c1614d4817154b4e6fbfb667ba2b231ea7aa53796d91f1800af9aeb703f59"
# FIXME: cfi testsuite sigill
hardening = ["vis"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _devel(self):
    return self.default_devel()
