pkgname = "python-cachetools"
pkgver = "7.0.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Extensible memoizing collections and decorators"
license = "MIT"
url = "https://github.com/tkem/cachetools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "daceb60e04f7b5a22812010b5984c9b20bb3ee0df99939aca8e547c5b08356c0"


def post_install(self):
    self.install_license("LICENSE")
