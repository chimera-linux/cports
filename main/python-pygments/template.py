pkgname = "python-pygments"
pkgver = "2.15.1"
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
sha256 = "8ace4d3c1dd481894b2005f560ead0f9f19ee64fe983366be1a21e171d12775c"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
