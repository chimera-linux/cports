pkgname = "python-trove-classifiers"
pkgver = "2025.8.6.13"
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
sha256 = "5a0abad839d2ed810f213ab133d555d267124ddea29f1d8a50d6eca12a50ae6e"
# cycle
options = ["!check"]
