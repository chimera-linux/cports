pkgname = "openexr"
pkgver = "3.2.1"
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
sha256 = "61e175aa2203399fb3c8c2288752fbea3c2637680d50b6e306ea5f8ffdd46a9b"
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
