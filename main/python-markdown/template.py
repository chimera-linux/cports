pkgname = "python-markdown"
pkgver = "3.3.4"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pyyaml"]
depends = ["python-setuptools"]
pkgdesc = "Python implementation of Markdown"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/Python-Markdown/markdown"
source = f"$(PYPI_SITE)/M/Markdown/Markdown-{pkgver}.tar.gz"
sha256 = "31b5b491868dcc87d6c24b7e3d19a0d730d59d3e46f4eea6430a321bed387a49"

def post_install(self):
    self.install_license("LICENSE.md")
