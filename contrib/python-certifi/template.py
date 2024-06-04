pkgname = "python-certifi"
pkgver = "2024.6.2"
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
sha256 = "3cd43f1c6fa7dedc5899d69d3ad0398fd018ad1a17fba83ddaf78aa46c747516"
# no tests
options = ["!check"]
