pkgname = "python-editables"
pkgver = "0.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-coverage", "python-pytest", "python-pytest-cov"]
depends = ["python"]
pkgdesc = "Editable installations for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pfmoore/editables"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "42f7240164af1e028ccb7b60e72f54bbd8b639e9409595fbeffac5d3fb610643"
# checkdepends missing
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
