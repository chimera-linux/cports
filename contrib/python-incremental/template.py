pkgname = "python-incremental"
pkgver = "24.7.2"
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
sha256 = "fb4f1d47ee60efe87d4f6f0ebb5f70b9760db2b2574c59c8e8912be4ebd464c9"
# circular with twisted
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
