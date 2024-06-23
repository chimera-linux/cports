pkgname = "python-hatchling"
pkgver = "1.25.0"
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
] + _deps
depends = list(_deps)
checkdepends = ["python-pytest"] + _deps
pkgdesc = "Python build backend used by Hatch"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://hatch.pypa.io/latest"
source = f"$(PYPI_SITE)/h/hatchling/hatchling-{pkgver}.tar.gz"
sha256 = "7064631a512610b52250a4d3ff1bd81551d6d1431c4eb7b72e734df6c74f4262"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
