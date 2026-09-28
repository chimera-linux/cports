pkgname = "python-pathspec"
pkgver = "1.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python utility library for pattern matching of file paths"
license = "MPL-2.0"
url = "https://github.com/cpburnz/python-pathspec"
source = f"$(PYPI_SITE)/p/pathspec/pathspec-{pkgver}.tar.gz"
sha256 = "17db5ecd524104a120e173814c90367a96a98d07c45b2e10c2f3919fff91bf5a"
# cycle
options = ["!check"]
