pkgname = "python-constantly"
pkgver = "15.1.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Symbolic constants for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/twisted/constantly"
source = f"$(PYPI_SITE)/c/constantly/constantly-{pkgver}.tar.gz"
sha256 = "586372eb92059873e29eba4f9dec8381541b4d3834660707faf8ba59146dfc35"


def post_install(self):
    self.install_license("LICENSE")
