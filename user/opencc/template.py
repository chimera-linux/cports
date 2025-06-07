pkgname = "opencc"
pkgver = "1.1.9"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DENABLE_GTEST=ON",
    "-DUSE_SYSTEM_GTEST=ON",
    "-DUSE_SYSTEM_MARISA=ON",
    "-DUSE_SYSTEM_RAPIDJSON=ON",
    "-DUSE_SYSTEM_TCLAP=ON",
]
# conditionally appended to below
make_check_args = []
hostmakedepends = ["pkgconf", "cmake", "ninja", "python"]
makedepends = ["gtest-devel", "marisa-trie-devel", "rapidjson", "tclap"]
pkgdesc = "Open Chinese conversion library"
license = "Apache-2.0"
url = "https://github.com/BYVoid/OpenCC"
source = f"{url}/archive/refs/tags/ver.{pkgver}.tar.gz"
sha256 = "ad4bcd8d87219a240a236d4a55c9decd2132a9436697d2882ead85c8939b0a99"

if self.profile().arch == "ppc64":
    # FIXME: hangs
    make_check_args += ["-E", "ConfigTest"]


@subpackage("opencc-devel")
def _(self):
    return self.default_devel()
