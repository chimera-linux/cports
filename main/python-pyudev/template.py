pkgname = "python-pyudev"
pkgver = "0.24.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "virtual:so:libudev.so.1!udev-libs"]
checkdepends = ["python-pytest", "udev-libs"]
pkgdesc = "Python bindings to libudev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/pyudev/pyudev"
source = f"$(PYPI_SITE)/p/pyudev/pyudev-{pkgver}.tar.gz"
sha256 = "b2a3afe1c99ea751f8296652557eac559874da2a1b1ec0625178706ec5a345f3"
# needs itself installed
options = ["!check"]
