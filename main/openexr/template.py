pkgname = "openexr"
pkgver = "3.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
make_check_args = [
    "-E",
    # fails to catch a divzero assert by wrong name
    "(OpenEXR.Iex"
    # require downloaded exr files to test against
    "|OpenEXR.bin)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "imath-devel",
    "libdeflate-devel",
]
pkgdesc = "Reference implementation of the EXR format"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://www.openexr.com"
source = f"https://github.com/openexr/openexr/archive/v{pkgver}.tar.gz"
sha256 = "b1b200606640547fceff0d3ebe01ac05c4a7ae2a131be7e9b3e5b9f491ef35b3"
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
