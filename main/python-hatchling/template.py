pkgname = "python-hatchling"
pkgver = "1.18.0"
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
sha256 = "50e99c3110ce0afc3f7bdbadff1c71c17758e476731c27607940cfa6686489ca"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
