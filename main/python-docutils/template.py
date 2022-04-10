pkgname = "python-docutils"
pkgver = "0.18.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pygments"]
depends = ["python-pygments"]
pkgdesc = "Python documentation utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none AND BSD-2-Clause AND GPL-3.0-or-later AND Python-2.0"
url = "http://docutils.sourceforge.net"
source = f"$(PYPI_SITE)/d/docutils/docutils-{pkgver}.tar.gz"
sha256 = "679987caf361a7539d76e584cbeddc311e3aee937877c87346f31debc63e9d06"

def do_check(self):
    self.do("python", "alltests.py", wrksrc = "test")

def post_install(self):
    self.install_license("COPYING.txt")

    for b in [
        "html", "html4", "html5", "latex", "man", "odt", "odt_prepstyles",
        "pseudoxml", "s5", "xetex", "xml"
    ]:
        self.install_link(f"rst2{b}.py", f"usr/bin/rst2{b}")

    self.install_link(f"rstpep2html.py", "usr/bin/rstpep2html")