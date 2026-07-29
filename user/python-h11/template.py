pkgname = "python-h11"
pkgver = "0.16.0"
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
pkgdesc = "Pure-Python HTTP/1.1 protocol implementation"
license = "MIT"
url = "https://github.com/python-hyper/h11"
source = f"https://pypi.io/packages/source/h/h11/h11-{pkgver}.tar.gz"
sha256 = "4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1"


def post_install(self):
    self.install_license("LICENSE.txt")
