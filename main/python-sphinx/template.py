pkgname = "python-sphinx"
pkgver = "7.0.1"
pkgrel = 1
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
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/S/Sphinx/Sphinx-{pkgver}.tar.gz"
sha256 = "61e025f788c5977d9412587e733733a289e2b9fdc2fef8868ddfbfc4ccfe881d"
# dependency of pytest, missing other checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
