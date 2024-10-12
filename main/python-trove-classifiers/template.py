pkgname = "python-trove-classifiers"
pkgver = "2024.10.12"
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
sha256 = "52528e3ed81d05ad81773251938ec84cc553e2bba688683f2e44b1c5f565b363"
# cycle
options = ["!check"]
