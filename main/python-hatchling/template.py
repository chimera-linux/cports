pkgname = "python-hatchling"
pkgver = "1.17.1"
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
sha256 = "76dee5108f929b7eb9102df0a1bf88fa3247d68a44ff1f395e1cf32eaab0c6fa"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
