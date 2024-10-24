pkgname = "python-pyproject-metadata"
pkgver = "0.9.0"
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
sha256 = "e23f57ee2c83e364badf6503a21e0d80db3440afe520b211c1d1e9060010f0f8"


def post_install(self):
    self.install_license("LICENSE")
