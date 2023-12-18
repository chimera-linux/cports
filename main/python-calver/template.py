pkgname = "python-calver"
pkgver = "2022.6.26"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Setuptools extension for CalVer package versions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/di/calver"
source = f"$(PYPI_SITE)/c/calver/calver-{pkgver}.tar.gz"
sha256 = "e05493a3b17517ef1748fbe610da11f10485faa7c416b9d33fd4a52d74894f8b"
# no tests
options = ["!check"]
