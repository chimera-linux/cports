pkgname = "python-flaky"
pkgver = "3.7.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Plugin for nose/pytest that reruns flaky tests"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/box/flaky"
source = f"$(PYPI_SITE)/f/flaky/flaky-{pkgver}.tar.gz"
sha256 = "3ad100780721a1911f57a165809b7ea265a7863305acb66708220820caf8aa0d"
# bunch more deps + broken
options = ["!check"]
