pkgname = "python-pyparsing"
pkgver = "3.0.7"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Python parsing module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyparsing/pyparsing"
source = f"{url}/archive/pyparsing_{pkgver}.tar.gz"
sha256 = "9303df2c7998485cc71a246c6cc0489c48ad571adc9d250c2d1314c47768ba59"
# calls urlopen
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
