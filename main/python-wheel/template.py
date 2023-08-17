pkgname = "python-wheel"
pkgver = "0.41.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "python-setuptools"]
pkgdesc = "Built-in package format for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "12b911f083e876e10c595779709f8a88a59f45aacc646492a67fe9ef796c1b47"
# TODO
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
