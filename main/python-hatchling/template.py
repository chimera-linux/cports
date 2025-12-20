pkgname = "python-hatchling"
pkgver = "1.28.0"
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
license = "MIT"
url = "https://hatch.pypa.io/latest"
source = f"$(PYPI_SITE)/h/hatchling/hatchling-{pkgver}.tar.gz"
sha256 = "4d50b02aece6892b8cd0b3ce6c82cb218594d3ec5836dbde75bf41a21ab004c8"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
