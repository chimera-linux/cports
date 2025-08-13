pkgname = "python-identify"
pkgver = "2.6.13"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-setuptools",
]
checkdepends = [
    "python-installer",
    "python-pytest",
    "python-ukkonen",
]
depends = [
    "python-ukkonen",
]
pkgdesc = "File identification library for Python"
license = "MIT"
url = "https://github.com/pre-commit/identify"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "93a51afb4721ebbcc46045af64e26b063fd691cfb966b26c21999e028eeeb12e"


def post_install(self):
    self.install_license("LICENSE")
