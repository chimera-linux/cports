pkgname = "python-hatchling"
pkgver = "1.29.0"
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
sha256 = "793c31816d952cee405b83488ce001c719f325d9cda69f1fc4cd750527640ea6"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
