pkgname = "python-sphinx"
pkgver = "7.4.4"
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
sha256 = "43c911f997a4530b6cffd4ff8d5516591f6c60d178591f4406f0dd02282e3f64"
# dependency of pytest, missing other checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")
