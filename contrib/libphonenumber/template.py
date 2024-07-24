pkgname = "libphonenumber"
pkgver = "8.13.42"
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
sha256 = "7fac3a3c5f37607108ea2ca4c334000a6c29fe1cd6b30db31505cba73ab96c7d"


@subpackage("libphonenumber-devel")
def _devel(self):
    self.depends += [
        "abseil-cpp-devel",
        "protobuf-devel",
    ]
    return self.default_devel()
