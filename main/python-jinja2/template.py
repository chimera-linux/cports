pkgname = "python-jinja2"
pkgver = "3.1.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = ["python", "python-markupsafe"]
pkgdesc = "Python template engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://jinja.pocoo.org"
source = f"$(PYPI_SITE)/J/Jinja2/Jinja2-{pkgver}.tar.gz"
sha256 = "ac8bd6544d4bb2c9792bf3a159e80bba8fda7f07e81bc3aed565432d5925ba90"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")
