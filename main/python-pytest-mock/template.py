pkgname = "python-pytest-mock"
pkgver = "3.14.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python-mock", "python-pytest"]
checkdepends = ["python-pytest-asyncio", *depends]
pkgdesc = "Thin-wrapper around the mock package for easier use with pytest"
license = "MIT"
url = "https://pytest-mock.readthedocs.io/en/latest/index.html"
source = f"$(PYPI_SITE)/p/pytest-mock/pytest_mock-{pkgver}.tar.gz"
sha256 = "159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e"


def post_install(self):
    self.install_license("LICENSE")
