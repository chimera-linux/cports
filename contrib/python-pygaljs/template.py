pkgname = "python-pygaljs"
pkgver = "1.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-setuptools"]
checkdepends = ["python-pytest"]
pkgdesc = (
    "Python package providing assets from https://github.com/Kozea/pygal.js"
)
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "LGPL-3.0-or-later"
url = "https://github.com/ionelmc/python-pygaljs"
_pygaljscommit = "28cef7c290896fcbac8d9e269778d75d9f0a6453"
source = [f"$(PYPI_SITE)/p/pygaljs/pygaljs-{pkgver}.tar.gz"]
sha256 = "0b71ee32495dcba5fbb4a0476ddbba07658ad65f5675e4ad409baf154dec5111"
