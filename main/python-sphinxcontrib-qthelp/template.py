pkgname = "python-sphinxcontrib-qthelp"
pkgver = "1.0.3"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Sphinx extension which outputs QtHelp document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://sphinx-doc.org"
source = (
    f"$(PYPI_SITE)/s/sphinxcontrib-qthelp/sphinxcontrib-qthelp-{pkgver}.tar.gz"
)
sha256 = "4c33767ee058b70dba89a6fc5c1892c0d57a54be67ddd3e7875a18d14cba5a72"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
