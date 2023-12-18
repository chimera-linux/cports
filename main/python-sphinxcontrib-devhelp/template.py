pkgname = "python-sphinxcontrib-devhelp"
pkgver = "1.0.2"
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
pkgdesc = "Sphinx extension which outputs Devhelp document"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/s/sphinxcontrib-devhelp/sphinxcontrib-devhelp-{pkgver}.tar.gz"
sha256 = "ff7f1afa7b9642e7060379360a67e9c41e8f3121f2ce9164266f61b9f4b338e4"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
