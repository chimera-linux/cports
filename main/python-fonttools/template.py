pkgname = "python-fonttools"
pkgver = "4.53.1"
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
sha256 = "d085ccabbb95144969f10fe4c801881dc404ad29ff1ae07d3631f35ec6a7c006"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
