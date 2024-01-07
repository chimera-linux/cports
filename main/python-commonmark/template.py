pkgname = "python-commonmark"
pkgver = "0.9.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = [
    "python-wheel",
    "python-flake8",
    "python-hypothesis",
    "python-colorama",
]
pkgdesc = "Python CommonMark Markdown parser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/rtfd/commonmark.py"
source = f"$(PYPI_SITE)/c/commonmark/commonmark-{pkgver}.tar.gz"
sha256 = "452f9dc859be7f06631ddcb328b6919c67984aca654e5fefb3914d54691aed60"
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
