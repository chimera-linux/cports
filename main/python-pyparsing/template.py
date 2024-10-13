pkgname = "python-pyparsing"
pkgver = "3.2.0"
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
sha256 = "91f52e4e06a2ee736531a3038fc2c7d6bb83f321831435fcedc14f95749c86ac"
# calls urlopen
options = ["!check"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")
