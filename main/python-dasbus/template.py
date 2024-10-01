pkgname = "python-dasbus"
pkgver = "1.7"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-gobject"]
checkdepends = ["dbus", "python-pytest", *depends]
pkgdesc = "Python DBus library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/rhinstaller/dasbus"
source = f"$(PYPI_SITE)/d/dasbus/dasbus-{pkgver}.tar.gz"
sha256 = "a8850d841adfe8ee5f7bb9f82cf449ab9b4950dc0633897071718e0d0036b6f6"
