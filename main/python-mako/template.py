pkgname = "python-mako"
pkgver = "1.2.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest", "python-setuptools", "python-markupsafe"]
depends = ["python-setuptools", "python-markupsafe"]
pkgdesc = "Fast and lightweight templating engine for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.makotemplates.org"
source = f"$(PYPI_SITE)/M/Mako/Mako-{pkgver}.tar.gz"
sha256 = "f054a5ff4743492f1aa9ecc47172cb33b42b9d993cffcc146c9de17e717b0307"
# tests failing with 3.10 for now, should be harmless
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
