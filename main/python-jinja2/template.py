pkgname = "python-jinja2"
pkgver = "3.1.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = ["python", "python-markupsafe"]
pkgdesc = "Python template engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://jinja.pocoo.org"
source = f"$(PYPI_SITE)/J/Jinja2/Jinja2-{pkgver}.tar.gz"
sha256 = "31351a702a408a9e7595a8fc6150fc3f43bb6bf7e319770cbc0db9df9437e852"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")
