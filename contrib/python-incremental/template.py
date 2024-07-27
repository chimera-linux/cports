pkgname = "python-incremental"
pkgver = "24.7.1"
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
sha256 = "a3717c20534499835555ba727b32ee087945ba9daaf23851471dfe3d1e3d1698"
# circular with twisted
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
