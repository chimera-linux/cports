pkgname = "python-hatchling"
pkgver = "1.21.0"
pkgrel = 1
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
sha256 = "5c086772357a50723b825fd5da5278ac7e3697cdf7797d07541a6c90b6ff754c"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
