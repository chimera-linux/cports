pkgname = "python-calver"
pkgver = "2025.4.17"
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
sha256 = "460702737d620f5c3d4175450485180a1b7f7a422c5db0e6af3e655c7395ec7e"
# no tests
options = ["!check"]
