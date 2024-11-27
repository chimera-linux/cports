pkgname = "python-pytest-expect"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-pytest",
    "python-u-msgpack",
]
pkgdesc = "Pytest plugin to store test expectations"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/gsnedders/pytest-expect"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8392093123dfc9807c28fee251e1d710aaed0d46ee77c7531528fb0a265eb798"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
