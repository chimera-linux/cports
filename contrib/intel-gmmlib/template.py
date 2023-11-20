pkgname = "intel-gmmlib"
pkgver = "22.3.14"
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
sha256 = "63b879a5a20756b6f74244068f4555a56c4f705c96cbc87e5163448a893e133f"
# FIXME: cfi testsuite sigill
hardening = ["vis"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _devel(self):
    return self.default_devel()
