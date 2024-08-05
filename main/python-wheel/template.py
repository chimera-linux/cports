pkgname = "python-wheel"
pkgver = "0.44.0"
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
sha256 = "a29c3f2817e95ab89aa4660681ad547c0e9547f20e75b0562fe7723c9a2a9d49"
# cylic
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
