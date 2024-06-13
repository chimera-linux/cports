pkgname = "libphonenumber"
pkgver = "8.13.39"
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
    "zlib-devel",
]
pkgdesc = "Library for parsing, formatting, and validating phone numbers"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/google/libphonenumber"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "700eb7a7b9a4bbd1c8aa757aaa7b0cc8c5047d4c33c48518564eb3f0938e193f"


@subpackage("libphonenumber-devel")
def _devel(self):
    self.depends += [
        "abseil-cpp-devel",
        "protobuf-devel",
    ]
    return self.default_devel()
