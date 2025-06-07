pkgname = "marisa-trie"
# match to python-marisa
pkgver = "0.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Matching algorithm with recursively implemented storage"
license = "BSD-2-Clause OR LGPL-2.1-or-later"
url = "https://github.com/s-yata/marisa-trie"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a3057d0c2da0a9a57f43eb8e07b73715bc5ff053467ee8349844d01da91b5efb"


def post_install(self):
    self.install_license("COPYING.md")


@subpackage("marisa-trie-devel")
def _(self):
    return self.default_devel()


@subpackage("marisa-trie-progs")
def _(self):
    return self.default_progs()
