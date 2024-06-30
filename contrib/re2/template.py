pkgname = "re2"
pkgver = "2024.07.01"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/google/re2"
source = f"{url}/archive/refs/tags/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "b767b92cd1e4d2f5eb3fea3401fdc3f45b7541fef59f0f516cc4e3b8f19afbdc"
tool_flags = {"CXXFLAGS": ["-DNDEBUG"]}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("re2-devel")
def _devel(self):
    return self.default_devel()
