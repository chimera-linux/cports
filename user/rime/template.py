pkgname = "rime"
pkgver = "1.13.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "boost-devel",
    "glog-devel",
    "leveldb-devel",
    "marisa-trie-devel",
    "opencc-devel",
    "yaml-cpp-devel",
]
checkdepends = ["gtest-devel"]
pkgdesc = "Rime Input Method Engine"
maintainer = "Bin Jin <bjin@protonmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/rime/librime"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "01e107c6e7f5767871585690b045ed1bba8a43e82c39f52e93fc2c381668dfb8"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("rime-devel")
def _(self):
    return self.default_devel()


@subpackage("rime-progs")
def _(self):
    return self.default_progs()
