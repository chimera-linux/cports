pkgname = "python-pip"
pkgver = "21.3.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-setuptools"]
pkgdesc = "Python package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pip.pypa.io"
source = f"$(PYPI_SITE)/p/pip/pip-{pkgver}.tar.gz"
sha256 = "fd11ba3d0fdb4c07fbc5ecbba0b1b719809420f25038f8ee3cd913d3faa3033a"
# unpackaged dependencies
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_link("pip3", "usr/bin/pip")
