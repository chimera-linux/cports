pkgname = "python-pip"
pkgver = "24.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "python-setuptools"]
pkgdesc = "Python package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://pip.pypa.io"
source = f"$(PYPI_SITE)/p/pip/pip-{pkgver}.tar.gz"
sha256 = "bdae551038c0ce6a83030b4aedef27fc95f0daa683593fea22fa05e55ed8e317"
# unpackaged dependencies
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
    # replace shim with symlink
    self.rm(self.destdir / "usr/bin/pip")
    self.install_link("usr/bin/pip", "pip3")
