pkgname = "python-certifi"
pkgver = "2024.12.14"
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
sha256 = "b650d30f370c2b724812bee08008be0c4163b163ddaec3f2546c1caf65f191db"
# no tests
options = ["!check"]
