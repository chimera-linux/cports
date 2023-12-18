pkgname = "python-pyparsing"
pkgver = "3.0.9"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-setuptools",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Python parsing module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pyparsing/pyparsing"
source = f"{url}/archive/pyparsing_{pkgver}.tar.gz"
sha256 = "7e8ce1684c517f57f945698fd3bbf86b36a2e60cd223f74886d3af04deb06306"
# calls urlopen
options = ["!check"]


def do_build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")
