pkgname = "python-sortedcollections"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-sortedcontainers"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Sorted collections library for Python"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "Apache-2.0"
url = "https://www.grantjenks.com/docs/sortedcollections"
source = f"https://github.com/grantjenks/python-sortedcollections/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4a70235d04737268feaed645e11c4aa25d165f0c69114f92d71e84ecb3e99ccf"
