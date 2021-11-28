pkgname = "python-pyparsing"
pkgver = "3.0.6"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Python parsing module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyparsing/pyparsing"
source = f"{url}/archive/pyparsing_{pkgver}.tar.gz"
sha256 = "b229816613fb9a05667d49934c60d34b26767666ed7dafe431cacbca22b70457"
# calls urlopen
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE")
