pkgname = "python-pycodestyle"
pkgver = "2.12.1"
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
sha256 = "231f65fbf5558e342cbad275245accb8a988d637cbeaf66508dd890f3d2d60fa"


def post_install(self):
    self.install_license("LICENSE")
