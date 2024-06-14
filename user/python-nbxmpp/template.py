pkgname = "python-nbxmpp"
pkgver = "5.0.4"
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
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://dev.gajim.org/gajim/python-nbxmpp"
source = f"$(PYPI_SITE)/n/nbxmpp/nbxmpp-{pkgver}.tar.gz"
sha256 = "166ea10ff643dae7911b764393d3baf5298062b431d48ac67a439436c861d611"
