pkgname = "python-smartypants"
pkgver = "2.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-docutils", "python-pytest"]
pkgdesc = "Translate ASCII punctuation into HTML entities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/leohemsted/smartypants.py"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b98191911ff3b4144ef8ad53e776a2d0ad24bd508a905c6ce523597c40022773"


def post_install(self):
    self.install_license("COPYING")
