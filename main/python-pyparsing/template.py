pkgname = "python-pyparsing"
pkgver = "3.2.3"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Python parsing module"
license = "MIT"
url = "https://github.com/pyparsing/pyparsing"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "3ad3397385c3f68c89d313529af4cafc9a9117845bc0cb6b38f02e621d151d38"
# calls urlopen
options = ["!check"]


def build(self):
    self.do("python", "-m", "flit_core.wheel")


def post_install(self):
    self.install_license("LICENSE")
