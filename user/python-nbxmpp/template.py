pkgname = "python-nbxmpp"
pkgver = "6.0.0"
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
sha256 = "5049a30222670edabcbd7d8ed657063e240d2cec0d3cdb19c8098e676f35f80a"
