pkgname = "python-hatchling"
pkgver = "1.21.1"
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
sha256 = "bba440453a224e7d4478457fa2e8d8c3633765bafa02975a6b53b9bf917980bc"
# no tests?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
