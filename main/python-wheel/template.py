pkgname = "python-wheel"
pkgver = "0.38.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "python-setuptools"]
pkgdesc = "Built-in package format for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "3d492ef22379a156ec923d2a77051cedfd4df4b667864e9e41ba83f0b70b7149"
# TODO
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
