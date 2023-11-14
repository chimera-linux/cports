pkgname = "python-trove-classifiers"
pkgver = "2023.11.13"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "python-calver",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Canonical source for classifiers on PyPI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/pypa/trove-classifiers"
source = f"$(PYPI_SITE)/t/trove-classifiers/trove-classifiers-{pkgver}.tar.gz"
sha256 = "87d8599d890b719c81c7e33cdb2813d5965e5958984bff1b913e161f0d6a5286"
# cycle
options = ["!check"]
