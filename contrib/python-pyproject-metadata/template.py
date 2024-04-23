pkgname = "python-pyproject-metadata"
pkgver = "0.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest"]
depends = ["python-packaging"]
pkgdesc = "PEP 621 metadata parsing"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://github.com/pypa/pyproject-metadata"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bb5015c9f3869c6fa59d8fdf29840a58cda2a570cb557b8aecae0f9e97a4cf88"


def post_install(self):
    self.install_license("LICENSE")
