pkgname = "python-calver"
pkgver = "2025.10.20"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
pkgdesc = "Setuptools extension for CalVer package versions"
license = "Apache-2.0"
url = "https://github.com/di/calver"
source = f"$(PYPI_SITE)/c/calver/calver-{pkgver}.tar.gz"
sha256 = "c98b376c2424642224d456b2f70c51402343e008c63d204634665e1a2a2835f5"
# no tests
options = ["!check"]
