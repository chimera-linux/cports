pkgname = "python-pyparsing"
pkgver = "3.1.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Python parsing module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyparsing/pyparsing"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "852644f146a0f90bb61f41ffb3572d4268d6f51a7242f8e2dac873cbc17963f4"
# calls urlopen
options = ["!check"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")
