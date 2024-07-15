pkgname = "python-sphinx"
pkgver = "7.4.3"
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
    "python-snowballstemmer",
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
sha256 = "bd846bcb09fd2b6e94ce3e1ad50f4618bccf03cc7c17d0f3fa87393c0bd9178b"
# dependency of pytest, missing other checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")
