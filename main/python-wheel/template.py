pkgname = "python-wheel"
pkgver = "0.45.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = [
    "python-devel",
    "python-pytest",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Built-in package format for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "a57353941a3183b3d5365346b567a260a0602a0f8a635926a7dede41b94c674a"
# cylic
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
