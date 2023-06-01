pkgname = "python-pip"
pkgver = "23.1.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "python-setuptools"]
pkgdesc = "Python package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pip.pypa.io"
source = f"$(PYPI_SITE)/p/pip/pip-{pkgver}.tar.gz"
sha256 = "0e7c86f486935893c708287b30bd050a36ac827ec7fe5e43fe7cb198dd835fba"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_link("pip3", "usr/bin/pip")
