pkgname = "python-pathspec"
pkgver = "0.11.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-flit_core",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python utility library for pattern matching of file paths"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://github.com/cpburnz/python-pathspec"
source = f"$(PYPI_SITE)/p/pathspec/pathspec-{pkgver}.tar.gz"
sha256 = "e0d8d0ac2f12da61956eb2306b69f9469b42f4deb0f3cb6ed47b9cce9996ced3"
# cycle
options = ["!check"]
