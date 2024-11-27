pkgname = "python-pyacoustid"
pkgver = "1.3.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "chromaprint",
    "python-audioread",
    "python-requests",
]
pkgdesc = "Python bindings for Chromaprint and Acoustid"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/beetbox/pyacoustid"
source = (
    f"https://github.com/beetbox/pyacoustid/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "405310612b178f42e7e933d1ad41e63c6b7fb9c6c900da9ee5e317c87ffb18fd"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
