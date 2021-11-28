pkgname = "python-babel"
pkgver = "2.9.1"
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
sha256 = "bc0c176f9f6a994582230df350aa6e05ba2ebe4b3ac317eab29d9be5d2768da0"
# needs pytest, is a dependency of pytest
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE")
