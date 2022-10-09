pkgname = "python-sphinx"
pkgver = "5.2.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-setuptools", "python-flit_core", "python-pip"]
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
sha256 = "5b10cb1022dac8c035f75767799c39217a05fc0fe2d6fe5597560d38e44f0363"
# dependency of pytest, missing other checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
