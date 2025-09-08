pkgname = "re2"
pkgver = "2025.08.05"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DRE2_USE_ICU=ON",
    "-DRE2_BUILD_TESTING=ON",
]
# takes literally forever
make_check_args = ["-E", "(exhaustive.*)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "abseil-cpp-devel",
    "benchmark-devel",
    "gtest-devel",
    "icu-devel",
]
pkgdesc = "C++ regular expression library"
license = "BSD-3-Clause"
url = "https://github.com/google/re2"
source = f"{url}/archive/refs/tags/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "b5708d8388110624c85f300e7e9b39c4ed5469891eb1127dd7f9d61272d04907"
tool_flags = {"CXXFLAGS": ["-DNDEBUG"]}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("re2-devel")
def _(self):
    return self.default_devel()
