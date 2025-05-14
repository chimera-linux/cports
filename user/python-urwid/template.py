pkgname = "python-urwid"
pkgver = "3.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-wcwidth"]
checkdepends = [*depends, "python-pytest"]
pkgdesc = "Console user interface library for Python"
license = "LGPL-2.1-only"
url = "http://urwid.org"
source = f"$(PYPI_SITE)/u/urwid/urwid-{pkgver}.tar.gz"
sha256 = "e7cb70ba1e7ff45779a5a57e43c57581ee7de6ceefb56c432491a4a6ce81eb78"
# unpackaged dependencies
options = ["!check"]
