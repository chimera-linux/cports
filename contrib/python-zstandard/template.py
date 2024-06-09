pkgname = "python-zstandard"
pkgver = "0.22.0"
pkgrel = 1
build_style = "python_pep517"
make_build_args = ["--skip-dependency-check"]
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python bindings to the Zstandard compression library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://github.com/indygreg/python-zstandard"
source = f"{url}/releases/download/{pkgver}/zstandard-{pkgver}.tar.gz"
sha256 = "8226a33c542bcb54cd6bd0a366067b610b41713b64c9abec1bc4533d69f51e70"
# tests fail to find internal modules due to cwd
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
