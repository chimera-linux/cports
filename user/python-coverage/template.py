pkgname = "python-coverage"
pkgver = "7.17.2"
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
]
pkgdesc = "Code coverage tool for python"
license = "Apache-2.0"
url = "https://coverage.readthedocs.io"
source = f"https://github.com/coveragepy/coveragepy/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "af6118d0af152c9e59fb27065a5b84b08ed526189ce31f4157eccc5c39a0ae3c"
