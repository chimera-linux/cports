pkgname = "python-pkgconfig"
pkgver = "1.5.5"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-poetry-core", "python-installer"]
depends = ["pkgconf", "python"]
checkdepends = [
    "openssl3-devel",
    "python-pytest",
    "python-setuptools",
    *depends,
]
pkgdesc = "Python interface to pkg-config"
license = "MIT"
url = "https://github.com/matze/pkgconfig"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "58ee1926b23ddb766a55eb9932441201a60e8e476d3798d0c5def167604f3b6c"


def post_install(self):
    self.install_license("LICENSE")
