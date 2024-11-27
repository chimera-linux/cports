# python-marisa-trie is a different pypi module
pkgname = "python-marisa"
# match to marisa-trie
pkgver = "0.2.6"
pkgrel = 1
build_wrksrc = "bindings/python"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "swig",
]
makedepends = ["marisa-trie-devel"]
depends = ["python"]
pkgdesc = "Python bindings for libmarisa"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause OR LGPL-2.1-or-later"
url = "https://github.com/s-yata/marisa-trie"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1063a27c789e75afa2ee6f1716cc6a5486631dcfcb7f4d56d6485d2462e566de"
# no tests
options = ["!check"]


def pre_build(self):
    self.do("make", "-C", "..", "swig-python")


def post_install(self):
    self.install_license("../../COPYING.md")
