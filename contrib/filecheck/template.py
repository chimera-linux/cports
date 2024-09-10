pkgname = "filecheck"
pkgver = "1.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Reimplementation of LLVM FileCheck in Python"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/AntonLydike/filecheck"
# pypi has no tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "229c1b4f34aae1538d6d0ba2cf2d8cd09b77db51297236d893307f95231a296e"
