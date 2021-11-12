pkgname = "python-babel"
pkgver = "2.8.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-setuptools", "python-pytz"]
pkgdesc = "Tools for internationalizing Python applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://babel.pocoo.org"
source = f"$(PYPI_SITE)/B/Babel/Babel-{pkgver}.tar.gz"
sha256 = "1aac2ae2d0d8ea368fa90906567f5c08463d98ade155c0c4bfedd6a0f7160e38"

def post_install(self):
    self.install_license("LICENSE")
