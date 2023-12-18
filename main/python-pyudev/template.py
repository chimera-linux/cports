pkgname = "python-pyudev"
pkgver = "0.24.1"
pkgrel = 1
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
sha256 = "75e54d37218f5ac45b0da1f0fd9cc5e526a3cac3ef1cfad410cf7ab338b01471"
# needs itself installed
options = ["!check"]
