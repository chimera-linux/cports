pkgname = "python-hatchling"
pkgver = "1.20.0"
pkgrel = 0
build_style = "python_pep517"
_deps = [
    "python-packaging",
    "python-editables",
    "python-pathspec",
    "python-pluggy",
    "python-trove-classifiers",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
] + _deps
depends = list(_deps)
checkdepends = ["python-pytest"] + _deps
pkgdesc = "Python build backend used by Hatch"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://hatch.pypa.io/latest"
source = f"$(PYPI_SITE)/h/hatchling/hatchling-{pkgver}.tar.gz"
sha256 = "0e0893cbe3d5f9275fc0e5b629087fc23b17abd7065e4db0a310e0a0237bc945"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
