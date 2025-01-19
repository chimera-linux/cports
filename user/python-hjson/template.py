pkgname = "python-hjson"
pkgver = "3.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-setuptools"]
depends = ["python"]
pkgdesc = "Hjson for Python"
maintainer = "Julie Koubova <julie@koubova.net>"
license = "MIT"
url = "https://github.com/hjson/hjson-py"
source = f"$(PYPI_SITE)/h/hjson/hjson-{pkgver}.tar.gz"
sha256 = "55af475a27cf83a7969c808399d7bccdec8fb836a07ddbd574587593b9cdcf75"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
