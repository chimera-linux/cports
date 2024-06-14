pkgname = "python-nbxmpp"
pkgver = "5.0.1"
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
checkdepends = depends + ["python-pytest"]
pkgdesc = "XMPP Library"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://dev.gajim.org/gajim/python-nbxmpp"
source = f"$(PYPI_SITE)/n/nbxmpp/nbxmpp-{pkgver}.tar.gz"
sha256 = "6aa5c7519e00241feb18085315a26a451a42dac23286fda8c35711a2f1350719"
