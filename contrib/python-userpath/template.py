pkgname = "python-userpath"
pkgver = "1.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Python module for adding locations to PATH"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/ofek/userpath"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "62abb8073f1db2b530704106e9126a7434fdc9abad4c9743682f14672920e093"


def post_install(self):
    self.install_license("LICENSE.txt")
