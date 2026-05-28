# test if sphinx doesn't break on updates (e.g. qemu build)
pkgname = "python-docutils"
pkgver = "0.23"
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
sha256 = "746f5060322511280a1e50eb76846ed6bf2342984b2ac04dc42caa1a8d78799e"


def check(self):
    self.do("python", "alltests.py", wrksrc="test")


def post_install(self):
    self.install_license("COPYING.rst")
