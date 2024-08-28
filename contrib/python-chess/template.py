pkgname = "python-chess"
pkgver = "1.10.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["stockfish"]
pkgdesc = "Pure Python chess library with move generation and validation"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/niklasf/python-chess"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "832fa7d589ffe916f5e84f08ece0d634dfb50568867932e525edcebb573041df"


def check(self):
    self.do("python", "setup.py", "test")
