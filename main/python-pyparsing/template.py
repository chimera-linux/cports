pkgname = "python-pyparsing"
pkgver = "3.1.2"
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
source = f"{url}/archive/pyparsing_{pkgver}.tar.gz"
sha256 = "9655507e4583fa20d2b6909ce4bf7fee71a9976ea94c734dd857fa9ae7c9c7dd"
# calls urlopen
options = ["!check"]


def do_build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")
