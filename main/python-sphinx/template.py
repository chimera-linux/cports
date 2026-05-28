pkgname = "python-sphinx"
pkgver = "9.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = [
    "python",
    "python-alabaster",
    "python-babel",
    "python-docutils",
    "python-imagesize",
    "python-jinja2",
    "python-packaging",
    "python-pygments",
    "python-requests",
    "python-roman-numerals",
    "python-snowballstemmer",
    "python-sphinxcontrib-applehelp",
    "python-sphinxcontrib-devhelp",
    "python-sphinxcontrib-htmlhelp",
    "python-sphinxcontrib-jsmath",
    "python-sphinxcontrib-qthelp",
    "python-sphinxcontrib-serializinghtml",
]
pkgdesc = "Python documentation generator"
license = "BSD-3-Clause"
url = "https://www.sphinx-doc.org/en/master"
source = f"$(PYPI_SITE)/s/sphinx/sphinx-{pkgver}.tar.gz"
sha256 = "7741722357dd75f8190766926071fed3bdc211c74dd2d7d4df5404da95930ddb"
# dependency of pytest, missing other checkdepends
options = ["!check"]

# satisfy build system
hostmakedepends += [*depends]


def post_install(self):
    self.install_license("LICENSE.rst")
