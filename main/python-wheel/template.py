pkgname = "python-wheel"
pkgver = "0.46.1"
pkgrel = 1
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
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "fd477efb5da0f7df1d3c76c73c14394002c844451bd63229d8570f376f5e6a38"
# cylic
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
