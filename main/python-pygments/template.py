pkgname = "python-pygments"
pkgver = "2.11.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Generic syntax highlighter written in Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pygments.org"
source = f"$(PYPI_SITE)/P/Pygments/Pygments-{pkgver}.tar.gz"
sha256 = "4e426f72023d88d03b2fa258de560726ce890ff3b630f88c21cbb8b2503b8c6a"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
