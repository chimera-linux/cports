pkgname = "python-userpath"
pkgver = "1.9.1"
pkgrel = 1
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
sha256 = "9a8d42168d961c15a07e12074b860c660234d320eb98bbacf03e8a498739a59a"


def post_install(self):
    self.install_license("LICENSE.txt")
