pkgname = "python-identify"
pkgver = "2.6.14"
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
sha256 = "14bbd7da84110b4bbeab623b32ed61848c4e1d75dc74a95d933832e7ce5a1453"


def post_install(self):
    self.install_license("LICENSE")
