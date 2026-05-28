pkgname = "python-wheel"
pkgver = "0.47.0"
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
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "cc72bd1009ba0cf63922e28f94d9d83b920aa2bb28f798a31d0691b02fa3c9b3"
# cylic
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
