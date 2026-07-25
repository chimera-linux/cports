pkgname = "python-urwid"
pkgver = "4.0.7"
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
sha256 = "c31aff787741428028b20bac3b0774fbe4f10de00ae00fe07722244d09462248"
