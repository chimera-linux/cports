pkgname = "python-babel"
pkgver = "2.12.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytz"]
depends = ["python", "python-setuptools", "python-pytz"]
pkgdesc = "Tools for internationalizing Python applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://babel.pocoo.org"
source = f"$(PYPI_SITE)/B/Babel/Babel-{pkgver}.tar.gz"
sha256 = "cc2d99999cd01d44420ae725a21c9e3711b3aadc7976d6147f622d8581963455"
# needs pytest, is a dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
