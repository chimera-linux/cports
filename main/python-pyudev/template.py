pkgname = "python-pyudev"
pkgver = "0.23.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["eudev-libs"]
checkdepends = ["python-pytest", "eudev-libs"]
pkgdesc = "Python bindings to libudev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/pyudev/pyudev"
source = f"$(PYPI_SITE)/p/pyudev/pyudev-{pkgver}.tar.gz"
sha256 = "32ae3585b320a51bc283e0a04000fd8a25599edb44541e2f5034f6afee5d15cc"
# needs itself installed
options = ["!check"]
