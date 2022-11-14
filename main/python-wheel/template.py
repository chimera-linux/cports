pkgname = "python-wheel"
pkgver = "0.38.4"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "python-setuptools"]
pkgdesc = "Built-in package format for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "965f5259b566725405b05e7cf774052044b1ed30119b5d586b2703aafe8719ac"
# TODO
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")
