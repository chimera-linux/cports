pkgname = "python-jinja2"
pkgver = "3.0.3"
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
sha256 = "611bb273cd68f3b993fabdc4064fc858c5b47a973cb5aa7999ec1ba405c87cd7"
# dependency of pytest
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE.rst")
