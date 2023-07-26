pkgname = "python-wheel"
pkgver = "0.41.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "python-setuptools"]
pkgdesc = "Built-in package format for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "55a0f0a5a84869bce5ba775abfd9c462e3a6b1b7b7ec69d72c0b83d673a5114d"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
