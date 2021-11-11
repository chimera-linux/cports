pkgname = "python-jinja2"
pkgver = "3.0.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = ["python-markupsafe"]
pkgdesc = "Python template engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://jinja.pocoo.org"
source = f"$(PYPI_SITE)/J/Jinja2/Jinja2-{pkgver}.tar.gz"
sha256 = "827a0e32839ab1600d4eb1c4c33ec5a8edfbc5cb42dafa13b81f182f97784b45"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.rst")
