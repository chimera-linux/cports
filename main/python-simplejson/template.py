pkgname = "python-simplejson"
pkgver = "3.20.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python JSON encoder and decoder"
license = "MIT OR AFL-2.1"
url = "https://simplejson.readthedocs.io"
source = f"$(PYPI_SITE)/s/simplejson/simplejson-{pkgver}.tar.gz"
sha256 = "e64139b4ec4f1f24c142ff7dcafe55a22b811a74d86d66560c8815687143037d"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")
