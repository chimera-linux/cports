pkgname = "re2"
pkgver = "2025.07.22"
pkgrel = 0
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
sha256 = "f54c29f1c3e13e12693e3d6d1230554df3ab3a1066b2e1f28c5330bfbf6db1e3"
tool_flags = {"CXXFLAGS": ["-DNDEBUG"]}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("re2-devel")
def _(self):
    return self.default_devel()
