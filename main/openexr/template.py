pkgname = "openexr"
pkgver = "3.2.4"
pkgrel = 2
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.openexr.com"
source = f"https://github.com/openexr/openexr/archive/v{pkgver}.tar.gz"
sha256 = "81e6518f2c4656fdeaf18a018f135e96a96e7f66dbe1c1f05860dd94772176cc"
# CIF: has a bunch of test failures
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("openexr-devel")
def _(self):
    self.depends += ["imath-devel"]
    return self.default_devel()


@subpackage("openexr-libs")
def _(self):
    return self.default_libs()
