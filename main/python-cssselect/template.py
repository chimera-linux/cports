pkgname = "python-cssselect"
pkgver = "1.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = [
    "python-lxml",
    "python-pytest",
]
pkgdesc = "Python module for CSS selectors"
license = "BSD-3-Clause"
url = "https://cssselect.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/c/cssselect/cssselect-{pkgver}.tar.gz"
sha256 = "57f8a99424cfab289a1b6a816a43075a4b00948c86b4dcf3ef4ee7e15f7ab0c7"


def post_install(self):
    self.install_license("LICENSE")
