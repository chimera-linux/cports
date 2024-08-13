pkgname = "python-lark-parser"
pkgver = "1.2.1"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/lark-parser/lark"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6e74e07b35829809e846e5d2b1e5b806394b35a8ad2569e1df45dd8d49b71681"


def post_install(self):
    self.install_license("LICENSE")
