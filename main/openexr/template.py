pkgname = "openexr"
pkgver = "3.2.2"
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
sha256 = "65de6459c245a4977ce4d7777e70b30d7ef48ec38e0cfb10205706ca50a8bf2e"
# FIXME: cfi has a bunch of test failures
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("openexr-devel")
def _devel(self):
    self.depends += ["imath-devel"]
    return self.default_devel()


@subpackage("openexr-libs")
def _libs(self):
    return self.default_libs()
