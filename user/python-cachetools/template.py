pkgname = "python-cachetools"
pkgver = "6.2.0"
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
sha256 = "f2b8a896891276a3b3dda4f78d49c93e5dbdb08757c02098d4757c8d6cec2fc1"


def post_install(self):
    self.install_license("LICENSE")
