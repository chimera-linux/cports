pkgname = "python-sphinx"
pkgver = "6.1.3"
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
url = "http://sphinx-doc.org"
source = f"$(PYPI_SITE)/S/Sphinx/Sphinx-{pkgver}.tar.gz"
sha256 = "0dac3b698538ffef41716cf97ba26c1c7788dba73ce6f150c1ff5b4720786dd2"
# dependency of pytest, missing other checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
