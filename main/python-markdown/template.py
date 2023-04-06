pkgname = "python-markdown"
pkgver = "3.4.3"
pkgrel = 0
build_style = "python_pep517"
make_install_target = f"Markdown-{pkgver}-*-*-*.whl"
hostmakedepends = ["python-pip", "python-flit_core", "python-wheel"]
checkdepends = ["python-pyyaml", "python-pytest"]
depends = ["python"]
pkgdesc = "Python implementation of Markdown"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/Python-Markdown/markdown"
source = f"$(PYPI_SITE)/M/Markdown/Markdown-{pkgver}.tar.gz"
sha256 = "8bf101198e004dc93e84a12a7395e31aac6a9c9942848ae1d99b9d72cf9b3520"
# checkdepends missing
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.md")
