pkgname = "python-pip"
pkgver = "22.0.4"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python-setuptools"]
pkgdesc = "Python package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pip.pypa.io"
source = f"$(PYPI_SITE)/p/pip/pip-{pkgver}.tar.gz"
sha256 = "b3a9de2c6ef801e9247d1527a4b16f92f2cc141cd1489f3fffaf6a9e96729764"
# unpackaged dependencies
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_link("pip3", "usr/bin/pip")
