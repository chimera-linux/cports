pkgname = "python-syrupy"
pkgver = "4.7.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-pytest"]
checkdepends = [*depends]
pkgdesc = "Pytest snapshot plugin"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://tophat.github.io/syrupy"
source = f"$(PYPI_SITE)/s/syrupy/syrupy-{pkgver}.tar.gz"
sha256 = "f9d4485f3f27d0e5df6ed299cac6fa32eb40a441915d988e82be5a4bdda335c8"
# unpackaged dependencies
options = ["!check"]
