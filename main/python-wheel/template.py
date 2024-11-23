pkgname = "python-wheel"
pkgver = "0.45.1"
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
sha256 = "661e1abd9198507b1409a20c02106d9670b2576e916d58f520316666abca6729"
# cylic
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
