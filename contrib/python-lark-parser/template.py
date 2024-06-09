pkgname = "python-lark-parser"
pkgver = "1.1.9"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Parsing toolkit for Python"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/lark-parser/lark"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "32f5f3e1418df3a9032d1a8f9bea62427319e28733ac463f5f37d311b1d99c01"


def post_install(self):
    self.install_license("LICENSE")
