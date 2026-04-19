pkgname = "python-pathspec"
pkgver = "1.0.4"
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
sha256 = "0210e2ae8a21a9137c0d470578cb0e595af87edaa6ebf12ff176f14a02e0e645"
# cycle
options = ["!check"]
