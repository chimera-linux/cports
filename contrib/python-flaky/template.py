pkgname = "python-flaky"
pkgver = "3.8.0"
pkgrel = 0
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
sha256 = "3b4b9f5c15829c919c8e05b15582fa1c9c7f20a303581dd5d0bc56a66441389c"
# bunch more deps + broken
options = ["!check"]
