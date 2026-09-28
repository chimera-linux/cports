pkgname = "python-re-assert"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-regex"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Show where your regex match assertion failed"
license = "MIT"
url = "https://github.com/asottile/re-assert"
# pypi does not have tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "01c4a849ed520923e4bab9afdf73b5f2698c4f92ad7f580ccb3f68ea79c69c0c"


def post_install(self):
    self.install_license("LICENSE")
