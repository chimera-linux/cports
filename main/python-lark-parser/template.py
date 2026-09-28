pkgname = "python-lark-parser"
pkgver = "1.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Parsing toolkit for Python"
license = "MIT"
url = "https://github.com/lark-parser/lark"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7e6ee0e0e650643150ee42622d28e77324fe413eb83037817f05add5236356b2"


def post_install(self):
    self.install_license("LICENSE")
