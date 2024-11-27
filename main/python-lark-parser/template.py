pkgname = "python-lark-parser"
pkgver = "1.2.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Parsing toolkit for Python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/lark-parser/lark"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "472a686b2cf8034938e9fd5df98afd09ae8781e837bfd74abb18d161cc504a82"


def post_install(self):
    self.install_license("LICENSE")
