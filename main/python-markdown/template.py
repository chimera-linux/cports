pkgname = "python-markdown"
pkgver = "3.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pyyaml", "python-pytest"]
depends = ["python"]
pkgdesc = "Python implementation of Markdown"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/Python-Markdown/markdown"
source = f"$(PYPI_SITE)/M/Markdown/Markdown-{pkgver}.tar.gz"
sha256 = "ed4f41f6daecbeeb96e576ce414c41d2d876daa9a16cb35fa8ed8c2ddfad0224"
# checkdepends missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
