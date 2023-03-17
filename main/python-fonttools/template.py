pkgname = "python-fonttools"
pkgver = "4.39.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "f49a6d3cf67c44a2e8da4435f42e736cbc96591c7033f86ab9f778b11b266b17"
# unpackaged deps
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
