pkgname = "python-certifi"
pkgver = "2024.7.4"
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
sha256 = "5a1e7645bc0ec61a09e26c36f6106dd4cf40c6db3a1fb6352b0244e7fb057c7b"
# no tests
options = ["!check"]
