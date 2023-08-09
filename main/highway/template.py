pkgname = "highway"
pkgver = "1.0.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DHWY_SYSTEM_GTEST=ON",
    "-DHWY_ENABLE_EXAMPLES=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gtest-devel"]
pkgdesc = "Google's SIMD library with runtime dispatch"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/google/highway"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "99b7dad98b8fa088673b720151458fae698ae5df9154016e39de4afdc23bb927"
# FIXME: cfi breaks a few tests
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("highway-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libhwy_contrib")
def _contrib(self):
    return [
        "usr/lib/libhwy_contrib.so.*",
    ]


@subpackage("libhwy_test")
def _test(self):
    return [
        "usr/lib/libhwy_test.so.*",
    ]
