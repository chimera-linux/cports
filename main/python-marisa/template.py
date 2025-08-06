# python-marisa-trie is a different pypi module
pkgname = "python-marisa"
# match to marisa-trie
pkgver = "0.3.1"
pkgrel = 0
build_wrksrc = "bindings/python"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "swig",
]
makedepends = ["marisa-trie-devel", "python-devel"]
depends = ["python"]
pkgdesc = "Python bindings for libmarisa"
license = "BSD-2-Clause OR LGPL-2.1-or-later"
url = "https://github.com/s-yata/marisa-trie"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "986ed5e2967435e3a3932a8c95980993ae5a196111e377721f0849cad4e807f3"
# no tests
options = ["!check"]


def pre_build(self):
    self.do("make", "-C", "..", "swig-python")


def post_install(self):
    self.install_license("../../COPYING.md")
