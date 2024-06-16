pkgname = "python-pycodestyle"
pkgver = "2.12.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python style guide checker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/PyCQA/pycodestyle"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c72dccf2bf7ceb603b5bd8b737a511d5241e675e90d4f75bc8a12fe81f24c094"


def post_install(self):
    self.install_license("LICENSE")
