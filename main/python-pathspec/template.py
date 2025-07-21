pkgname = "python-pathspec"
pkgver = "0.12.1"
pkgrel = 2
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
sha256 = "a482d51503a1ab33b1c67a6c3813a26953dbdc71c31dacaef9a838c4e29f5712"
# cycle
options = ["!check"]
