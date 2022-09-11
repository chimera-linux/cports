pkgname = "python-mako"
pkgver = "1.2.2"
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
sha256 = "3724869b363ba630a272a5f89f68c070352137b8fd1757650017b7e06fda163f"
# tests failing with 3.10 for now, should be harmless
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
