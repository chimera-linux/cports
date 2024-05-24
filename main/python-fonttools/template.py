pkgname = "python-fonttools"
pkgver = "4.52.1"
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
sha256 = "91f965e97b5e06b146354b15298534c4bc593e8a0b030187376d516c9846ff3c"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
