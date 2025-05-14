pkgname = "toot"
pkgver = "0.48.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools_scm",
]
depends = [
    "python-beautifulsoup4",
    "python-click",
    "python-dateutil",
    "python-pillow",
    "python-requests",
    "python-term-image",
    "python-tomlkit",
    "python-urwid",
    "python-urwidgets",
]
checkdepends = [
    *depends,
    "python-pytest",
]
pkgdesc = "CLI tool for interacting with the fediverse"
license = "GPL-3.0-or-later"
url = "https://github.com/ihabunek/toot"
source = f"$(PYPI_SITE)/t/toot/toot-{pkgver}.tar.gz"
sha256 = "99629e24bc4ef3fb22162b7742f4053648279f5e7e34b5ad53224b5d3e05a66c"
