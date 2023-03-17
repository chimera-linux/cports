pkgname = "python-fonttools"
pkgver = "4.39.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "35ba12c2cf7722f5dc34c5bfe6f3f96f8a858db5849b5d3315725e7561e91ed1"
# unpackaged deps
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
