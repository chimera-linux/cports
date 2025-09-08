pkgname = "abseil-cpp"
pkgver = "20250814.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_CXX_STANDARD=17",
    "-DBUILD_SHARED_LIBS=ON",
    "-DABSL_PROPAGATE_CXX_STD=ON",
    "-DABSL_USE_EXTERNAL_GOOGLETEST=ON",
    "-DABSL_BUILD_TESTING=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["linux-headers", "gtest-devel"]
pkgdesc = "Abseil C++ libraries"
license = "Apache-2.0"
url = "https://abseil.io"
source = (
    f"https://github.com/abseil/abseil-cpp/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "9b2b72d4e8367c0b843fa2bcfa2b08debbe3cee34f7aaa27de55a6cbb3e843db"


@subpackage("abseil-cpp-testing")
def _(self):
    self.subdesc = "testing libraries"

    return [
        "usr/lib/libabsl_*_helper*.so.*",
        "usr/lib/libabsl_*_mock_*.so.*",
        "usr/lib/libabsl_*_test_*.so.*",
        "usr/lib/libabsl_*_testing.so.*",
        "usr/lib/libabsl_stack_consumption.so.*",
        "usr/lib/libabsl_test_*.so.*",
    ]


@subpackage("abseil-cpp-devel")
def _(self):
    return self.default_devel()
