pkgname = "openexr"
pkgver = "3.3.5"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
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
license = "BSD-3-Clause"
url = "https://www.openexr.com"
source = f"https://github.com/openexr/openexr/archive/v{pkgver}.tar.gz"
sha256 = "cb0c88710c906c9bfc59027eb147e780d508c7be1a90b43af3ec9e3c2987b70d"
# CIF: has a bunch of test failures
hardening = ["vis", "!cfi"]

_exclude_tests = [
    # fails to catch a divzero assert by wrong name
    "OpenEXR.Iex",
    # require downloaded exr files to test against
    "OpenEXR.bin",
]

if self.profile().arch == "armv7":
    # bus error
    _exclude_tests.append("OpenEXR.testLargeDataWindowOffsets")

make_check_args = ["-E", f"({'|'.join(_exclude_tests)})"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("openexr-devel")
def _(self):
    self.depends += ["imath-devel"]
    return self.default_devel()


@subpackage("openexr-libs")
def _(self):
    return self.default_libs()
