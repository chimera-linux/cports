pkgname = "python-certifi"
pkgver = "2025.1.31"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["ca-certificates", "python"]
pkgdesc = "Python package for providing Mozilla's CA bundle"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/certifi/python-certifi"
source = f"$(PYPI_SITE)/c/certifi/certifi-{pkgver}.tar.gz"
sha256 = "3d5da6925056f6f18f119200434a4780a94263f10d1c21d032a6f6b2baa20651"
# no tests
options = ["!check"]
