pkgname = "python-fonttools"
pkgver = "4.41.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c3b247bad5f11f20475eb7ab68ea1600b459ddde16dbed434bc4f9ad645ee9b3"
# unpackaged deps
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
