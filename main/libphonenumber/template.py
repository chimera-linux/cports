pkgname = "libphonenumber"
pkgver = "9.0.25"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # stupid cmake target stuff, don't require -devel-static
    "-DBUILD_STATIC_LIB=OFF",
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
license = "Apache-2.0"
url = "https://github.com/google/libphonenumber"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "de4cfebe1e1da4ecfb687c7bdf312d93b37548737f5e52444d2d29d0b36d2512"


@subpackage("libphonenumber-devel")
def _(self):
    self.depends += [
        "abseil-cpp-devel",
        "protobuf-devel",
    ]
    return self.default_devel()
