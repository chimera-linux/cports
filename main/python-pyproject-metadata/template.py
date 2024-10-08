pkgname = "python-pyproject-metadata"
pkgver = "0.8.1"
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
sha256 = "dec0ca7f8c70633595af5b9904e429ab6d15b8d35b633942843b044139d64c27"


def post_install(self):
    self.install_license("LICENSE")
