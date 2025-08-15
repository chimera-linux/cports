pkgname = "python-cachetools"
pkgver = "6.1.0"
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
sha256 = "356b6354ceef47bc31466654343cf4250084f53b6ef04aa3fd3b583d4a16871c"


def post_install(self):
    self.install_license("LICENSE")
