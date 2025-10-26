pkgname = "librime"
pkgver = "1.14.0"
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
sha256 = "b2b29c3551eec6b45af1ba8fd3fcffb99e2b7451aa974c1c9ce107e69ce3ea68"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("librime-devel")
def _(self):
    return self.default_devel()


@subpackage("librime-progs")
def _(self):
    return self.default_progs()
