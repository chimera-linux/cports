pkgname = "python-nbxmpp"
pkgver = "6.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "glib",
    "libsoup",
    "python-gobject",
    "python-idna",
    "python-packaging",
    "python-precis-i18n",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "XMPP Library"
license = "GPL-3.0-or-later"
url = "https://dev.gajim.org/gajim/python-nbxmpp"
source = f"$(PYPI_SITE)/n/nbxmpp/nbxmpp-{pkgver}.tar.gz"
sha256 = "ab09d3afc8d7f589c97a27e5b884d467d1cf98c7239740c8e9504c5c47071811"
