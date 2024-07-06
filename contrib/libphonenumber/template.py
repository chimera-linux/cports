pkgname = "libphonenumber"
pkgver = "8.13.40"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DREGENERATE_METADATA=OFF",
    "-DUSE_BOOST=OFF",
    "-DUSE_STDMUTEX=ON",
]
make_check_target = "tests"
cmake_dir = "cpp"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "abseil-cpp-devel",
    "gtest-devel",
    "icu-devel",
    "protobuf-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for parsing, formatting, and validating phone numbers"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/google/libphonenumber"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0d6733f842c30e5b3762ec1478f1da2f27a7661ae2e6bbe38b8c07ae4dd2277b"


@subpackage("libphonenumber-devel")
def _devel(self):
    self.depends += [
        "abseil-cpp-devel",
        "protobuf-devel",
    ]
    return self.default_devel()
