pkgname = "python-nbxmpp"
pkgver = "6.1.1"
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
    "python-idna",
    "python-packaging",
    "python-precis-i18n",
    "python-gobject",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "XMPP Library"
license = "GPL-3.0-or-later"
url = "https://dev.gajim.org/gajim/python-nbxmpp"
source = f"$(PYPI_SITE)/n/nbxmpp/nbxmpp-{pkgver}.tar.gz"
sha256 = "b6f3e03046460cd67f4b2b43edbb648d04ff85d244828a7b387924f9a3e65ae6"
