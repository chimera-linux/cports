pkgname = "python-pyproject-metadata"
pkgver = "0.7.1"
pkgrel = 0
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
source = f"https://github.com/FFY00/python-pyproject-metadata/archive/refs/tags/{pkgver}.zip"
sha256 = "10ddb9479c14e07a369f8dafded14aaf765a9f1ebb2f309a92ca59c3e936ef43"


def post_install(self):
    self.install_license("LICENSE")
