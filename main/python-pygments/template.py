pkgname = "python-pygments"
pkgver = "2.10.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "Generic syntax highlighter written in Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pygments.org"
source = f"$(PYPI_SITE)/P/Pygments/Pygments-{pkgver}.tar.gz"
sha256 = "f398865f7eb6874156579fdf36bc840a03cab64d1cde9e93d68f46a425ec52c6"
# dependency of pytest
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE")
