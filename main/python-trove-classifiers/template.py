pkgname = "python-trove-classifiers"
pkgver = "2025.9.11.17"
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
sha256 = "931ca9841a5e9c9408bc2ae67b50d28acf85bef56219b56860876dd1f2d024dd"
# cycle
options = ["!check"]
