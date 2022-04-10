pkgname = "python-jinja2"
pkgver = "3.1.1"
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
sha256 = "640bed4bb501cbd17194b3cace1dc2126f5b619cf068a726b98192a0fde74ae9"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.rst")
