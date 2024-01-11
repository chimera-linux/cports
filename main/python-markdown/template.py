pkgname = "python-markdown"
pkgver = "3.5.2"
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
sha256 = "e1ac7b3dc550ee80e602e71c1d168002f062e49f1b11e26a36264dafd4df2ef8"
# checkdepends missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
