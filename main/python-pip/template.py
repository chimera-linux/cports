pkgname = "python-pip"
pkgver = "24.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python", "python-setuptools"]
pkgdesc = "Python package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pip.pypa.io"
source = f"$(PYPI_SITE)/p/pip/pip-{pkgver}.tar.gz"
sha256 = "ebcb60557f2aefabc2e0f918751cd24ea0d56d8ec5445fe1807f1d2109660b99"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
    # replace shim with symlink
    self.uninstall("usr/bin/pip")
    self.install_link("usr/bin/pip", "pip3")
