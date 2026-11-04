pkgname = "python-titlecase"
pkgver = "2.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python library to capitalize strings"
license = "MIT"
url = "https://github.com/ppannuto/python-titlecase"
source = f"$(PYPI_SITE)/t/titlecase/titlecase-{pkgver}.tar.gz"
sha256 = "7d83a277ccbbda11a2944e78a63e5ccaf3d32f828c594312e4862f9a07f635f5"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
