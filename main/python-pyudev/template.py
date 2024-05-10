pkgname = "python-pyudev"
pkgver = "0.24.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "virtual:so:libudev.so.1!udev-libs"]
checkdepends = ["python-pytest", "udev-libs"]
pkgdesc = "Python bindings to libudev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/pyudev/pyudev"
source = f"$(PYPI_SITE)/p/pyudev/pyudev-{pkgver}.tar.gz"
sha256 = "2e945427a21674893bb97632401db62139d91cea1ee96137cc7b07ad22198fc7"
# needs itself installed
options = ["!check"]
