pkgname = "python-iterable-io"
pkgver = "1.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python library to adapt iterables to a file-like interface"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-3.0-only"
url = "https://github.com/pR0Ps/iterable-io"
source = f"$(PYPI_SITE)/i/iterable-io/iterable-io-{pkgver}.tar.gz"
sha256 = "fb9e1b739587a9ba0d5c60a3e1eb71246761583bc9f18b3c35bb112b44b18c3c"
