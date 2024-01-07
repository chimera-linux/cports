pkgname = "python-editables"
pkgver = "0.5"
pkgrel = 1
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
sha256 = "1ff2663aa1669eb89115a38e2d4067c21bb847e7006f72bf979a1a91b8bc2304"
# checkdepends missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
