pkgname = "python-babel"
pkgver = "2.11.0"
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
sha256 = "5ef4b3226b0180dedded4229651c8b0e1a3a6a2837d45a073272f313e4cf97f6"
# needs pytest, is a dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

# FIXME visibility
hardening = ["!vis"]
