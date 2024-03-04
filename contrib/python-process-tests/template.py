pkgname = "python-process-tests"
pkgver = "3.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-setuptools"]
checkdepends = ["python-pytest"]
pkgdesc = "Tools for testing processes"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "BSD-2-Clause"
url = "https://github.com/ionelmc/python-process-tests"
source = f"$(PYPI_SITE)/p/process-tests/process-tests-{pkgver}.tar.gz"
sha256 = "e5d57dea7161251e91cadb84bf3ecc85275fb121fd478e579f800777b1d424bd"


def post_install(self):
    self.install_license("LICENSE")
