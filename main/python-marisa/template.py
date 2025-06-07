# python-marisa-trie is a different pypi module
pkgname = "python-marisa"
# match to marisa-trie
pkgver = "0.3.0"
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
sha256 = "a3057d0c2da0a9a57f43eb8e07b73715bc5ff053467ee8349844d01da91b5efb"
# no tests
options = ["!check"]


def pre_build(self):
    self.do("make", "-C", "..", "swig-python")


def post_install(self):
    self.install_license("../../COPYING.md")
