pkgname = "python-markdown"
pkgver = "3.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-flit_core",
    "python-wheel",
]
checkdepends = ["python-pyyaml", "python-pytest"]
depends = ["python"]
pkgdesc = "Python implementation of Markdown"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/Python-Markdown/markdown"
source = f"$(PYPI_SITE)/M/Markdown/Markdown-{pkgver}.tar.gz"
sha256 = "a807eb2e4778d9156c8f07876c6e4d50b5494c5665c4834f67b06459dfd877b3"
# checkdepends missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
