pkgname = "python-flaky"
pkgver = "3.8.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Plugin for nose/pytest that reruns flaky tests"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/box/flaky"
source = f"$(PYPI_SITE)/f/flaky/flaky-{pkgver}.tar.gz"
sha256 = "47204a81ec905f3d5acfbd61daeabcada8f9d4031616d9bcb0618461729699f5"
# bunch more deps + broken
options = ["!check"]
