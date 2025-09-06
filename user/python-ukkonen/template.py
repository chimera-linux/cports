pkgname = "python-ukkonen"
pkgver = "1.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-setuptools",
]
makedepends = [
    "python-devel",
]
checkdepends = [
    "python-installer",
    "python-pytest",
]
depends = [
    "python-cffi",
]
pkgdesc = "Implementation of bounded Levenshtein distance for Python"
license = "MIT"
url = "https://github.com/asottile/ukkonen"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5f3fd0e9c1b2a7ea669382ec3928370f11882cec991c4d3757955b56d18895f6"


def post_install(self):
    self.install_license("LICENSE")
