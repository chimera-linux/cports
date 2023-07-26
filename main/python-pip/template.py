pkgname = "python-pip"
pkgver = "23.2.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "python-setuptools"]
pkgdesc = "Python package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pip.pypa.io"
source = f"$(PYPI_SITE)/p/pip/pip-{pkgver}.tar.gz"
sha256 = "fb0bd5435b3200c602b5bf61d2d43c2f13c02e29c1707567ae7fbc514eb9faf2"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_link("pip3", "usr/bin/pip")
