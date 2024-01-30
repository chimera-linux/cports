pkgname = "python-pygal"
pkgver = "3.0.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-setuptools"]
pkgdesc = "Dynamic SVG charting library written in Python"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "LGPL-3.0-or-later"
url = "https://www.pygal.org/en/stable"
source = f"$(PYPI_SITE)/p/pygal/pygal-{pkgver}.tar.gz"
sha256 = "6c5da33f1041e8b30cbc980f8a34910d9edc584b833240298f6a25df65425289"
# tests require pytest-runner which is deprecated
options = ["!check"]
