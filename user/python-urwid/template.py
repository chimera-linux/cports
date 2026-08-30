pkgname = "python-urwid"
pkgver = "4.0.13"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
]
depends = ["python-wcwidth"]
checkdepends = [
    "python-gobject",
    "python-pyserial",
    "python-pytest",
    "python-trio",
    "python-twisted",
    *depends,
]
pkgdesc = "Console UI library"
license = "LGPL-2.1-or-later"
url = "https://urwid.org"
source = f"$(PYPI_SITE)/u/urwid/urwid-{pkgver}.tar.gz"
sha256 = "23afb15197b9e3b656b8c55bb3e18d50463c34db1982ec81ef5034525bea6c76"
