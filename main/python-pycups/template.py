pkgname = "python-pycups"
pkgver = "2.0.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["cups-devel", "python-devel"]
depends = ["python"]
pkgdesc = "Python bindings for CUPS"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/OpenPrinting/pycups"
source = f"$(PYPI_SITE)/p/pycups/pycups-{pkgver}.tar.gz"
sha256 = "843e385c1dbf694996ca84ef02a7f30c28376035588f5fbeacd6bae005cf7c8d"
# No test suite
options = ["!check"]
