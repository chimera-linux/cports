pkgname = "python-editables"
pkgver = "0.5"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Editable installations for Python"
license = "MIT"
url = "https://github.com/pfmoore/editables"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1ff2663aa1669eb89115a38e2d4067c21bb847e7006f72bf979a1a91b8bc2304"
# cycle
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
