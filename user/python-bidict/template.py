pkgname = "python-bidict"
pkgver = "0.23.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = [
    "python-hypothesis",
    "python-pytest",
    "python-pytest-benchmark",
    "python-pytest-xdist",
    "python-sortedcollections",
    "python-typing_extensions",
]
depends = ["python"]
pkgdesc = "Bidirectional mapping library for Python"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "MPL-2.0"
url = "https://bidict.readthedocs.io"
source = f"https://github.com/jab/bidict/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b3619436e1e1e3cba15856839666edcb769fce97b47f5bba5e2789b03eed3156"
