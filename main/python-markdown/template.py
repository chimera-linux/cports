pkgname = "python-markdown"
pkgver = "3.3.6"
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
sha256 = "76df8ae32294ec39dcf89340382882dfa12975f87f45c3ed1ecdb1e8cefc7006"
options = ["lto"]

def post_install(self):
    self.install_license("LICENSE.md")
