pkgname = "python-zstandard"
pkgver = "0.23.0"
pkgrel = 0
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
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f29233338bcef11f233737eb58aba85074f0fd3163bec1a20303de1270e6fb16"
# tests fail to find internal modules due to cwd
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
