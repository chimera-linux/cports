pkgname = "python-css-parser"
pkgver = "1.0.10"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "CSS Cascading Style Sheets library for Python"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/ebook-utils/css-parser"
source = f"$(PYPI_SITE)/c/css-parser/css-parser-{pkgver}.tar.gz"
sha256 = "bf1e972ad33344e93206964fb4cd908d9ddef9fcd0c01fa93e0d734675394363"
