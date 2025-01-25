pkgname = "opencc"
pkgver = "1.1.9"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DENABLE_GTEST=ON",
    "-DUSE_SYSTEM_GTEST=ON",
    "-DUSE_SYSTEM_MARISA=ON",
    "-DUSE_SYSTEM_RAPIDJSON=ON",
    "-DUSE_SYSTEM_TCLAP=ON",
]
hostmakedepends = ["pkgconf", "cmake", "ninja", "python"]
makedepends = ["marisa-trie-devel", "rapidjson", "tclap"]
checkdepends = ["gtest-devel"]
pkgdesc = "Open Chinese conversion library"
maintainer = "metalparade <comer@live.cn>"
license = "Apache-2.0"
url = "https://github.com/BYVoid/OpenCC"
source = f"{url}/archive/refs/tags/ver.{pkgver}.tar.gz"
sha256 = "ad4bcd8d87219a240a236d4a55c9decd2132a9436697d2882ead85c8939b0a99"


@subpackage("opencc-devel")
def _(self):
    return self.default_devel()
