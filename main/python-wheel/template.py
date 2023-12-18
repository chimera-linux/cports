pkgname = "python-wheel"
pkgver = "0.42.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "python-setuptools"]
pkgdesc = "Built-in package format for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "c45be39f7882c9d34243236f2d63cbd58039e360f85d0913425fbd7ceea617a8"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
