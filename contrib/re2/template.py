pkgname = "re2"
pkgver = "2024.06.01"
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
sha256 = "7326c74cddaa90b12090fcfc915fe7b4655723893c960ee3c2c66e85c5504b6c"
tool_flags = {"CXXFLAGS": ["-DNDEBUG"]}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("re2-devel")
def _devel(self):
    return self.default_devel()
