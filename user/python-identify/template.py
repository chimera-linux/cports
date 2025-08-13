pkgname = "python-identify"
pkgver = "2.6.19"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-ukkonen"]
checkdepends = [
    "python-pytest",
    *depends,
]
pkgdesc = "File identification library for Python"
license = "MIT"
url = "https://github.com/pre-commit/identify"
# pypi does not have tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b939a2e57f1085886aab677c7b78d07ca02bf1186c8aeaa12021b596229e5195"


def post_install(self):
    self.install_license("LICENSE")
