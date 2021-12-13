pkgname = "python-fonttools"
pkgver = "4.28.3"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "44d8953e0b522c704afc8dd6a5ec2a86b58bca950e506f9c7e8b3c5f2c29eecd"
# unpackaged deps
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
