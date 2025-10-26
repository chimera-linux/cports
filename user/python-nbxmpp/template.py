pkgname = "python-nbxmpp"
pkgver = "6.3.1"
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
sha256 = "c418d52ad4f8f4095796997d0a92eb0098fe77431e406713042e158324a2564d"
