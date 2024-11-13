pkgname = "python-hatchling"
pkgver = "1.26.3"
pkgrel = 0
build_style = "python_pep517"
_deps = [
    "python-editables",
    "python-packaging",
    "python-pathspec",
    "python-pluggy",
    "python-trove-classifiers",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    *_deps,
]
depends = [*_deps]
checkdepends = ["python-pytest", *_deps]
pkgdesc = "Python build backend used by Hatch"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://hatch.pypa.io/latest"
source = f"$(PYPI_SITE)/h/hatchling/hatchling-{pkgver}.tar.gz"
sha256 = "b672a9c36a601a06c4e88a1abb1330639ee8e721e0535a37536e546a667efc7a"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
