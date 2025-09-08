pkgname = "librime"
pkgver = "1.13.1"
pkgrel = 2
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
sha256 = "ae7eb6335139c044e438299b2ab9a0f630e665e8f5fe1f30a9416a2d1325b84e"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("librime-devel")
def _(self):
    return self.default_devel()


@subpackage("librime-progs")
def _(self):
    return self.default_progs()
