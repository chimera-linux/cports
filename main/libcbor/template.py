pkgname = "libcbor"
pkgver = "0.10.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DWITH_EXAMPLES=OFF",
    "-DWITH_TESTS=ON",
]
make_check_args = [
    "-E",
    # FIXME: test_float/test_double subtests fail, probably libm difference
    "ctest_run_float_ctrl_encoders_test",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["cmocka-devel"]
pkgdesc = "CBOR serialization format implementation for C"
maintainer = "Val Packett <val@packett.cool>"
license = "MIT"
url = "https://github.com/pjk/libcbor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e75f712215d7b7e5c89ef322a09b701f7159f028b8b48978865725f00f79875b"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("libcbor-devel")
def _devel(self):
    return self.default_devel()
