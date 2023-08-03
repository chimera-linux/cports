pkgname = "python-semidbm"
pkgver = "0.5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "DBM interface for Python"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/jamesls/semidbm"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d1f10454d4f80d682e25964e93cc798df7a249efcb7eb8d5ebe71b104b34e77e"


def post_install(self):
    self.install_license("COPYING")
