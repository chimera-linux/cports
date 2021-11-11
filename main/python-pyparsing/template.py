pkgname = "python-pyparsing"
pkgver = "2.4.7"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Python parsing module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyparsing/pyparsing"
source = f"{url}/archive/pyparsing_{pkgver}.tar.gz"
sha256 = "6deecf4b95a49a5a9c89b4a4b1fcb73c1cba0e3265ec7b858adffcced229ba05"

def post_install(self):
    self.install_license("LICENSE")
