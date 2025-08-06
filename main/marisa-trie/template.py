pkgname = "marisa-trie"
# match to python-marisa
pkgver = "0.3.1"
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
sha256 = "986ed5e2967435e3a3932a8c95980993ae5a196111e377721f0849cad4e807f3"


def post_install(self):
    self.install_license("COPYING.md")


@subpackage("marisa-trie-devel")
def _(self):
    return self.default_devel()


@subpackage("marisa-trie-progs")
def _(self):
    return self.default_progs()
