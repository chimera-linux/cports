pkgname = "python-pycodestyle"
pkgver = "2.13.0"
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
license = "MIT"
url = "https://github.com/PyCQA/pycodestyle"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b1a4db0d9b8285f6643bcdb41362be6d6c94b891b13ead09c57a2513c46b717b"


def post_install(self):
    self.install_license("LICENSE")
