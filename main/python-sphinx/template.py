pkgname = "python-sphinx"
pkgver = "5.1.1"
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
sha256 = "ba3224a4e206e1fbdecf98a4fae4992ef9b24b85ebf7b584bb340156eaf08d89"
# dependency of pytest, missing other checkdepends
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
