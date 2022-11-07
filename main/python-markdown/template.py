pkgname = "python-markdown"
pkgver = "3.4.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pyyaml"]
depends = ["python", "python-setuptools"]
pkgdesc = "Python implementation of Markdown"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/Python-Markdown/markdown"
source = f"$(PYPI_SITE)/M/Markdown/Markdown-{pkgver}.tar.gz"
sha256 = "3b809086bb6efad416156e00a0da66fe47618a5d6918dd688f53f40c8e4cfeff"

def post_install(self):
    self.install_license("LICENSE.md")
