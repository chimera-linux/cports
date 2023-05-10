pkgname = "python-incremental"
pkgver = "22.10.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Library to version your Python objects"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/twisted/incremental"
source = f"$(PYPI_SITE)/i/incremental/incremental-{pkgver}.tar.gz"
sha256 = "912feeb5e0f7e0188e6f42241d2f450002e11bbc0937c65865045854c24c0bd0"

def post_install(self):
    self.install_license("LICENSE")
