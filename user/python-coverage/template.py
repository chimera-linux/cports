pkgname = "python-coverage"
pkgver = "7.16.2"
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
sha256 = "d4f5d82461b7ea40a2486ba6b9d48987408edd2bf6fe98cc98966de159333eb9"
