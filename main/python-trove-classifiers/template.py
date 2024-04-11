pkgname = "python-trove-classifiers"
pkgver = "2024.4.10"
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
sha256 = "49f40bb6a746b72a1cba4f8d55ee8252169cda0f70802e3fd24f04b7fb25a492"
# cycle
options = ["!check"]
