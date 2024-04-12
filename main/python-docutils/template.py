pkgname = "python-docutils"
pkgver = "0.21.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python", "python-pygments"]
checkdepends = ["python-pillow", "python-pygments"]
pkgdesc = "Python documentation utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none AND BSD-2-Clause AND GPL-3.0-or-later AND Python-2.0"
url = "http://docutils.sourceforge.net"
source = f"$(PYPI_SITE)/d/docutils/docutils-{pkgver}.tar.gz"
sha256 = "65249d8a5345bc95e0f40f280ba63c98eb24de35c6c8f5b662e3e8948adea83f"
# Some test files seem to be missing in the tarball
options = ["!check"]


def do_check(self):
    self.do("python", "alltests.py", wrksrc="test")


def post_install(self):
    self.install_license("COPYING.txt")
