pkgname = "python-docutils"
pkgver = "0.20.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pygments"]
depends = ["python", "python-pygments"]
pkgdesc = "Python documentation utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none AND BSD-2-Clause AND GPL-3.0-or-later AND Python-2.0"
url = "http://docutils.sourceforge.net"
source = f"$(PYPI_SITE)/d/docutils/docutils-{pkgver}.tar.gz"
sha256 = "f08a4e276c3a1583a86dce3e34aba3fe04d02bba2dd51ed16106244e8a923e3b"


def do_check(self):
    self.do("python", "alltests.py", wrksrc="test")


def post_install(self):
    self.install_license("COPYING.txt")

    for b in [
        "html",
        "html4",
        "html5",
        "latex",
        "man",
        "odt",
        "odt_prepstyles",
        "pseudoxml",
        "s5",
        "xetex",
        "xml",
    ]:
        self.install_link(f"rst2{b}.py", f"usr/bin/rst2{b}")

    self.install_link("rstpep2html.py", "usr/bin/rstpep2html")
