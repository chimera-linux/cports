pkgname = "python-sphinxcontrib-jsmath"
pkgver = "1.0.1"
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
pkgdesc = "Sphinx extension which renders math in HTML with JavaScript"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://sphinx-doc.org"
source = (
    f"$(PYPI_SITE)/s/sphinxcontrib-jsmath/sphinxcontrib-jsmath-{pkgver}.tar.gz"
)
sha256 = "a9925e4a4587247ed2191a22df5f6970656cb8ca2bd6284309578f2153e0c4b8"
# circular checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
