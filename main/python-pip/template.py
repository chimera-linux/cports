pkgname = "python-pip"
pkgver = "26.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Python package manager"
license = "MIT"
url = "https://pip.pypa.io"
source = f"$(PYPI_SITE)/p/pip/pip-{pkgver}.tar.gz"
sha256 = "c4037d8a277c89b320abe636d59f91e6d0922d08a05b60e85e53b296613346d8"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
    # replace shim with symlink
    self.uninstall("usr/bin/pip")
    self.install_link("usr/bin/pip", "pip3")
