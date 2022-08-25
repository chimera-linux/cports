pkgname = "python-babel"
pkgver = "2.10.3"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytz"]
depends = ["python-setuptools", "python-pytz"]
pkgdesc = "Tools for internationalizing Python applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://babel.pocoo.org"
source = f"$(PYPI_SITE)/B/Babel/Babel-{pkgver}.tar.gz"
sha256 = "7614553711ee97490f732126dc077f8d0ae084ebc6a96e23db1482afabdb2c51"
# needs pytest, is a dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
