pkgname = "python-pyparsing"
pkgver = "3.2.1"
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
sha256 = "f514be1b50afaba317ff42cbf41c9115127c4ed35825b61cdcfad43cdf79a95a"
# calls urlopen
options = ["!check"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")
