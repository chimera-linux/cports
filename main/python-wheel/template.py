pkgname = "python-wheel"
pkgver = "0.42.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/wheel"
source = f"$(PYPI_SITE)/w/wheel/wheel-{pkgver}.tar.gz"
sha256 = "c45be39f7882c9d34243236f2d63cbd58039e360f85d0913425fbd7ceea617a8"
# cylic
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
