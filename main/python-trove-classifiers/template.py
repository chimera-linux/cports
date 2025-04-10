pkgname = "python-trove-classifiers"
pkgver = "2025.3.19.19"
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
license = "Apache-2.0"
url = "https://github.com/pypa/trove-classifiers"
source = f"$(PYPI_SITE)/t/trove-classifiers/trove_classifiers-{pkgver}.tar.gz"
sha256 = "98e9d396fe908d5f43b7454fa4c43d17cd0fdadf046f45fb38a5e3af8d959ecd"
# cycle
options = ["!check"]
