# pypi name
pkgname = "python-filecheck"
pkgver = "0.0.24"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Reimplementation of LLVM FileCheck in Python"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/mull-project/FileCheck.py"
# pypi has no tests
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4a89468778e47a35ee413f83070188f47a1842f367de6dfb511cc390d635cf11"
