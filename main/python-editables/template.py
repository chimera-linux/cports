pkgname = "python-editables"
pkgver = "0.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-flit_core",
    "python-wheel",
]
checkdepends = ["python-coverage", "python-pytest", "python-pytest-cov"]
depends = ["python"]
pkgdesc = "Editable installations for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pfmoore/editables"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "dab62d96596cfbefb68af4fbf18a7e01579adf8c5760f4868d64b9c4cd67e2a1"
# checkdepends missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
