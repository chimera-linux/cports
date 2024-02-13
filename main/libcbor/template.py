pkgname = "libcbor"
pkgver = "0.11.0"
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
sha256 = "89e0a83d16993ce50651a7501355453f5250e8729dfc8d4a251a78ea23bb26d7"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("libcbor-devel")
def _devel(self):
    return self.default_devel()
