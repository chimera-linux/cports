pkgname = "python-fonttools"
pkgver = "4.37.4"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "811389458954ff6fe3a503b11c00eccc202019b9dfe42c85de59365a45e7855d"
# unpackaged deps
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
