pkgname = "python-sphinx"
pkgver = "7.3.7"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-setuptools",
    "python-flit_core",
    "python-build",
    "python-installer",
]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = [
    "python",
    "python-jinja2",
    "python-docutils",
    "python-pygments",
    "python-snowballstemmer",
    "python-babel",
    "python-alabaster",
    "python-imagesize",
    "python-requests",
    "python-packaging",
    "python-sphinxcontrib-applehelp",
    "python-sphinxcontrib-devhelp",
    "python-sphinxcontrib-htmlhelp",
    "python-sphinxcontrib-jsmath",
    "python-sphinxcontrib-qthelp",
    "python-sphinxcontrib-serializinghtml",
]
pkgdesc = "Python documentation generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.sphinx-doc.org/en/master"
source = f"$(PYPI_SITE)/s/sphinx/sphinx-{pkgver}.tar.gz"
sha256 = "a4a7db75ed37531c05002d56ed6948d4c42f473a36f46e1382b0bd76ca9627bc"
# dependency of pytest, missing other checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")
