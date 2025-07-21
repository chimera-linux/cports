pkgname = "python-nbxmpp"
pkgver = "6.2.0"
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
sha256 = "5ad792f1324edff5a62217cfb9279dbb54ac48177958ef484556b56e8fce7160"
