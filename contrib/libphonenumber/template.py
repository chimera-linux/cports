pkgname = "libphonenumber"
pkgver = "8.13.44"
pkgrel = 0
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
sha256 = "3d5ad67d9a5bd5b73bc0bfa8b9258503209d4683e62aae581db11dfaeac1ba0a"


@subpackage("libphonenumber-devel")
def _(self):
    self.depends += [
        "abseil-cpp-devel",
        "protobuf-devel",
    ]
    return self.default_devel()
