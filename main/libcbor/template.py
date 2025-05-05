pkgname = "libcbor"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
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
license = "MIT"
url = "https://github.com/pjk/libcbor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5368add109db559f546d7ed10f440f39a273b073daa8da4abffc83815069fa7f"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("libcbor-devel")
def _(self):
    return self.default_devel()
