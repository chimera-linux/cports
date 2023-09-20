pkgname = "python-trove-classifiers"
pkgver = "2023.9.19"
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
sha256 = "3e700af445c802f251ce2b741ee78d2e5dfa5ab8115b933b89ca631b414691c9"
# cycle
options = ["!check"]
