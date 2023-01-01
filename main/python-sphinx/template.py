pkgname = "python-sphinx"
pkgver = "5.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-setuptools", "python-flit_core", "python-pip"]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = [
    "python", "python-jinja2", "python-docutils", "python-pygments",
    "python-snowballstemmer", "python-babel", "python-alabaster",
    "python-imagesize", "python-requests", "python-packaging",
    "python-sphinxcontrib-applehelp", "python-sphinxcontrib-devhelp",
    "python-sphinxcontrib-htmlhelp", "python-sphinxcontrib-jsmath",
    "python-sphinxcontrib-qthelp", "python-sphinxcontrib-serializinghtml"
]
pkgdesc = "Python documentation generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/S/Sphinx/Sphinx-{pkgver}.tar.gz"
sha256 = "51026de0a9ff9fc13c05d74913ad66047e104f56a129ff73e174eb5c3ee794b5"
# dependency of pytest, missing other checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
