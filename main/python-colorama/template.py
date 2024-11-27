pkgname = "python-colorama"
pkgver = "0.4.6"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = [
    "python-mock",
    "python-pytest",
]
pkgdesc = "Colored text output for python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/tartley/colorama"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2d0543c3970840160b32656ab83d43b7f3533208c2c5f3ee5b839940d00af0bd"


def post_install(self):
    self.install_license("LICENSE.txt")
