pkgname = "python-pycups"
pkgver = "2.0.1"
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
sha256 = "57434ce5f62548eb12949ca8217f066f4eeb21a5d6ab8b13471dce350e380c90"
# No test suite
options = ["!check"]
