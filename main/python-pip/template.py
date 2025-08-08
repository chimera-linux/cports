pkgname = "python-pip"
pkgver = "25.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python", "python-setuptools"]
pkgdesc = "Python package manager"
license = "MIT"
url = "https://pip.pypa.io"
source = f"$(PYPI_SITE)/p/pip/pip-{pkgver}.tar.gz"
sha256 = "578283f006390f85bb6282dffb876454593d637f5d1be494b5202ce4877e71f2"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
    # replace shim with symlink
    self.uninstall("usr/bin/pip")
    self.install_link("usr/bin/pip", "pip3")
