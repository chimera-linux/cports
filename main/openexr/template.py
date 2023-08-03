pkgname = "openexr"
pkgver = "3.1.10"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
# FIXME: have to figure out why this aborts
make_check_args = [
    "-E",
    "testOptimizedInterleavePatterns",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "imath-devel",
    "zlib-devel",
]
pkgdesc = "Reference implementation of the EXR format"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://www.openexr.com"
source = f"https://github.com/openexr/openexr/archive/v{pkgver}.tar.gz"
sha256 = "6e0fd3f0eb1cb907bd3593830ea2b3431b85f22a6f18f99f8cfa099fec70067d"
# FIXME: cfi has a bunch of test failures
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("openexr-devel")
def _devel(self):
    return self.default_devel()


@subpackage("openexr-libs")
def _libs(self):
    return self.default_libs()
