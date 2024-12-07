pkgname = "coverage"
pkgver = "7.6.4"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["-k", "not VirtualenvTest"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "python-devel",
]
checkdepends = [
    "python-flaky",
    "python-hypothesis",
    "python-pytest",
    "python-pytest-xdist",
]
depends = [
    "python",
    self.with_pkgver("python-coverage"),
]
pkgdesc = "Tool for measuring Python code coverage"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://coverage.readthedocs.io"
source = f"$(PYPI_SITE)/c/coverage/coverage-{pkgver}.tar.gz"
sha256 = "29fc0f17b1d3fea332f8001d4558f8214af7f1d87a345f3a133c901d60347c73"


def pre_check(self):
    # generate some required test files
    self.do("python", "igor.py", "zip_mods")


@subpackage("python-coverage")
def _(self):
    self.subdesc = "Python module"
    return ["usr/lib"]
