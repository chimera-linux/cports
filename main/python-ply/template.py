pkgname = "python-ply"
pkgver = "3.11"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-six"]
pkgdesc = "Lex and Yacc for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.dabeaz.com/ply"
source = f"$(PYPI_SITE)/p/ply/ply-{pkgver}.tar.gz"
sha256 = "00c7c1aaa88358b9c765b6d3000c6eec0ba42abca5351b095321aef446081da3"
# FIXME: need some weird setup
options = ["!check"]


def post_install(self):
    self.install_license("README.md")
