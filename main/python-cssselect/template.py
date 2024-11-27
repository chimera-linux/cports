pkgname = "python-cssselect"
pkgver = "1.2.0"
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
    "python-lxml",
    "python-pytest",
]
pkgdesc = "Python module for CSS selectors"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://cssselect.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/c/cssselect/cssselect-{pkgver}.tar.gz"
sha256 = "666b19839cfaddb9ce9d36bfe4c969132c647b92fc9088c4e23f786b30f1b3dc"


def post_install(self):
    self.install_license("LICENSE")
