pkgname = "python-trove-classifiers"
pkgver = "2025.2.18.16"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-calver",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Canonical source for classifiers on PyPI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/pypa/trove-classifiers"
source = f"$(PYPI_SITE)/t/trove-classifiers/trove_classifiers-{pkgver}.tar.gz"
sha256 = "b1ee2e1668589217d4edf506743e28b1834da128f8a122bad522c02d837006e1"
# cycle
options = ["!check"]
