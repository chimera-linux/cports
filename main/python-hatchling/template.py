pkgname = "python-hatchling"
pkgver = "1.26.1"
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
sha256 = "8d956592e6c5d5df1f591be1e97a941c7b9ec6fd039f4c8624c29557bac034e9"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
