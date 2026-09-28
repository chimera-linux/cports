pkgname = "librime"
pkgver = "1.17.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "boost-devel",
    "glog-devel",
    "gtest-devel",
    "leveldb-devel",
    "marisa-trie-devel",
    "opencc-devel",
    "yaml-cpp-devel",
]
pkgdesc = "Rime Input Method Engine"
license = "BSD-3-Clause"
url = "https://github.com/rime/librime"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a60274da5d8b8a7187e6c7e9ba5023334ed7bdd182535e93c4e96de8cf188377"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("librime-devel")
def _(self):
    return self.default_devel()


@subpackage("librime-progs")
def _(self):
    return self.default_progs()
