pkgname = "python-pyudev"
pkgver = "0.24.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "so:libudev.so.1!udev-libs"]
checkdepends = ["python-pytest", "udev-libs"]
pkgdesc = "Python bindings to libudev"
license = "LGPL-2.1-or-later"
url = "https://github.com/pyudev/pyudev"
source = f"$(PYPI_SITE)/p/pyudev/pyudev-{pkgver}.tar.gz"
sha256 = "e788bb983700b1a84efc2e88862b0a51af2a995d5b86bc9997546505cf7b36bc"
# needs itself installed
options = ["!check"]
