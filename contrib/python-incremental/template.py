pkgname = "python-incremental"
pkgver = "24.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Library to version your Python objects"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/twisted/incremental"
source = f"$(PYPI_SITE)/i/incremental/incremental-{pkgver}.tar.gz"
sha256 = "530255006a8c283d3ad29f30468efc6d5d95747afd0b52a4e4a4ded6348d88f8"
# circular with twisted
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
