pkgname = "python-pycodestyle"
pkgver = "2.11.1"
pkgrel = 1
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
sha256 = "a01fdd890c6472eebc32e8baf21e29173c35776e765c64cc83ccd09b99dc5399"


def post_install(self):
    self.install_license("LICENSE")
