pkgname = "python-docutils"
pkgver = "0.19"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pygments"]
depends = ["python", "python-pygments"]
pkgdesc = "Python documentation utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none AND BSD-2-Clause AND GPL-3.0-or-later AND Python-2.0"
url = "http://docutils.sourceforge.net"
source = f"$(PYPI_SITE)/d/docutils/docutils-{pkgver}.tar.gz"
sha256 = "33995a6753c30b7f577febfc2c50411fec6aac7f7ffeb7c4cfe5991072dcf9e6"


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
