pkgname = "python-fonttools"
pkgver = "4.45.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4e52b0a765dc8294e6caf15c68cce59aa2b8ad4b33d08f611002fdbbd6b2fe9e"
# unpackaged deps
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
