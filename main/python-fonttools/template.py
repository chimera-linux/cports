pkgname = "python-fonttools"
pkgver = "4.38.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "764c569221fb437d0c3937d19d3e38e137d324f225fb30e54ef0aaa2d6f7a289"
# unpackaged deps
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")

# FIXME visibility
hardening = ["!vis"]
