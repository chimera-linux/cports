pkgname = "marisa-trie"
# match to python-marisa
pkgver = "0.2.6"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Matching algorithm with recursively implemented storage"
maintainer = "Nasado <hi@nasado.name>"
license = "BSD-2-Clause OR LGPL-2.1-or-later"
url = "https://github.com/s-yata/marisa-trie"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1063a27c789e75afa2ee6f1716cc6a5486631dcfcb7f4d56d6485d2462e566de"


def post_install(self):
    self.install_license("COPYING.md")


@subpackage("marisa-trie-devel")
def _(self):
    return self.default_devel()


@subpackage("marisa-trie-progs")
def _(self):
    return self.default_progs()
