pkgname = "python-cachetools"
pkgver = "6.2.1"
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
sha256 = "2d5ddb99ac024a693d729bbbcf86a6a811686813fe1ed9c3f83f6385beda063e"


def post_install(self):
    self.install_license("LICENSE")
