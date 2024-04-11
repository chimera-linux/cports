pkgname = "python-sphinx"
pkgver = "7.2.6"
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
sha256 = "9a5160e1ea90688d5963ba09a2dcd8bdd526620edbb65c328728f1b2228d5ab5"
# dependency of pytest, missing other checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
