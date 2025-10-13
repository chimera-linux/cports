# test if sphinx doesn't break on updates (e.g. qemu build)
pkgname = "python-docutils"
pkgver = "0.22.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python", "python-pygments"]
checkdepends = ["python-pygments"]
pkgdesc = "Python documentation utilities"
license = "custom:none AND BSD-2-Clause AND GPL-3.0-or-later AND Python-2.0"
url = "http://docutils.sourceforge.net"
source = f"$(PYPI_SITE)/d/docutils/docutils-{pkgver}.tar.gz"
sha256 = "9fdb771707c8784c8f2728b67cb2c691305933d68137ef95a75db5f4dfbc213d"


def check(self):
    self.do("python", "alltests.py", wrksrc="test")


def post_install(self):
    self.install_license("COPYING.rst")
