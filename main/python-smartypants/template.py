pkgname = "python-smartypants"
pkgver = "2.0.2"
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
license = "BSD-3-Clause"
url = "https://github.com/leohemsted/smartypants.py"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "560ae7485a27c288f5bd63131f5c3c7b8f0745f50e7c3f85f0bbc65d87799d19"


def post_install(self):
    self.install_license("COPYING")
