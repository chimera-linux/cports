pkgname = "python-fonttools"
pkgver = "4.53.0"
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
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "f48a1e557e4c64b3a61c7a599bae3a33b44c0bbd190d8feb130d23065b0dfe71"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
