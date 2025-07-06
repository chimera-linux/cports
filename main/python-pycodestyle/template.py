pkgname = "python-pycodestyle"
pkgver = "2.14.0"
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
sha256 = "ffcf4dc55f1e5fbdc6dd6acf5db0fd07ded534ae376eee23a742e1410b48d9ae"


def post_install(self):
    self.install_license("LICENSE")
