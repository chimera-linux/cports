pkgname = "python-sphinx"
pkgver = "8.3.0"
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
    "python-roman-numerals-py",
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
sha256 = "3bad4314a7fa72ce92344eaaa14c42ddf3177ee6a79c227e4ff8ae07d416f584"
# dependency of pytest, missing other checkdepends
options = ["!check"]

# satisfy build system
hostmakedepends += [*depends]


def post_install(self):
    self.install_license("LICENSE.rst")
