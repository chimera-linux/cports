pkgname = "python-pygments"
pkgver = "2.13.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Generic syntax highlighter written in Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pygments.org"
source = f"$(PYPI_SITE)/P/Pygments/Pygments-{pkgver}.tar.gz"
sha256 = "56a8508ae95f98e2b9bdf93a6be5ae3f7d8af858b43e02c5a2ff083726be40c1"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")

# FIXME visibility
hardening = ["!vis"]
