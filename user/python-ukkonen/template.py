pkgname = "python-ukkonen"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
depends = ["python-cffi"]
pkgdesc = "Implementation of bounded Levenshtein distance for Python"
license = "MIT"
url = "https://github.com/asottile/ukkonen"
# pypi does not have tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d238ac2751c967594a5ffd4d3e76a01ddcc63d01088a5c54e5fdd9e3cc7e1211"


def post_install(self):
    self.install_license("LICENSE")
