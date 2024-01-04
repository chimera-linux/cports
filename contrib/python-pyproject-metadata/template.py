pkgname = "python-pyproject-metadata"
pkgver = "0.7.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python-packaging"]
pkgdesc = "PEP 621 metadata parsing"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://https://pep621.readthedocs.io/index.html"
source = f"https://github.com/FFY00/python-pyproject-metadata/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ad7467871eea29206d7cca024ee31bf9c1b13f7b9bfdefe94b481c7b671a8954"


def post_install(self):
    self.install_license("LICENSE")
