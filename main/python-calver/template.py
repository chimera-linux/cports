pkgname = "python-calver"
pkgver = "2025.4.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Setuptools extension for CalVer package versions"
license = "Apache-2.0"
url = "https://github.com/di/calver"
source = f"$(PYPI_SITE)/c/calver/calver-{pkgver}.tar.gz"
sha256 = "f854bb865a070da3d45f989f812b2fb6847a10c2d5a7490490ec16832617a463"
# no tests
options = ["!check"]
