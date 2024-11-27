pkgname = "python-userpath"
pkgver = "1.9.2"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python-click"]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Python module for adding locations to PATH"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/ofek/userpath"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c5e0019949f432afe28a7809ddb2197fe027e909cde78744400e77986f3eb99d"


def post_install(self):
    self.install_license("LICENSE.txt")
