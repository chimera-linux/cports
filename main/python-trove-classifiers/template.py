pkgname = "python-trove-classifiers"
pkgver = "2025.5.9.12"
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
sha256 = "7ca7c8a7a76e2cd314468c677c69d12cc2357711fcab4a60f87994c1589e5cb5"
# cycle
options = ["!check"]
