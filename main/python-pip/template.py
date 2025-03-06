pkgname = "python-pip"
pkgver = "25.0.1"
pkgrel = 1
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
sha256 = "88f96547ea48b940a3a385494e181e29fb8637898f88d88737c5049780f196ea"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
    # replace shim with symlink
    self.uninstall("usr/bin/pip")
    self.install_link("usr/bin/pip", "pip3")
