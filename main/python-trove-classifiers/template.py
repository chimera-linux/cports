pkgname = "python-trove-classifiers"
pkgver = "2023.8.7"
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
sha256 = "c9f2a0a85d545e5362e967e4f069f56fddfd91215e22ffa48c66fb283521319a"
# cycle
options = ["!check"]
