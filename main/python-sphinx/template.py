pkgname = "python-sphinx"
pkgver = "4.5.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = [
    "python-jinja2", "python-docutils", "python-pygments",
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
sha256 = "7bf8ca9637a4ee15af412d1a1d9689fec70523a68ca9bb9127c2f3eeb344e2e6"
# dependency of pytest, missing other checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
