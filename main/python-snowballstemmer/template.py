pkgname = "python-snowballstemmer"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Snowball stemming library collection for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://jinja.pocoo.org"
source = f"$(PYPI_SITE)/s/snowballstemmer/snowballstemmer-{pkgver}.tar.gz"
sha256 = "e997baa4f2e9139951b6f4c631bad912dfd3c792467e2f03d7239464af90e914"

def post_install(self):
    self.install_license("COPYING")
