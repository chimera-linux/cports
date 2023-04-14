pkgname = "python-pygments"
pkgver = "2.15.0"
pkgrel = 0
build_style = "python_pep517"
make_install_target = f"Pygments-{pkgver}-*-*-*.whl"
hostmakedepends = ["python-pip", "python-flit_core", "python-wheel"]
depends = ["python"]
pkgdesc = "Generic syntax highlighter written in Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://pygments.org"
source = f"$(PYPI_SITE)/P/Pygments/Pygments-{pkgver}.tar.gz"
sha256 = "f7e36cffc4c517fbc252861b9a6e4644ca0e5abadf9a113c72d1358ad09b9500"
# dependency of pytest
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
