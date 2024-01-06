pkgname = "python-pytest-mock"
pkgver = "3.12.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-mock", "python-pytest"]
checkdepends = ["python-pytest-asyncio"] + depends
pkgdesc = "Thin-wrapper around the mock package for easier use with pytest"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MIT"
url = "https://pytest-mock.readthedocs.io/en/latest/index.html"
source = f"$(PYPI_SITE)/p/pytest-mock/pytest-mock-{pkgver}.tar.gz"
sha256 = "31a40f038c22cad32287bb43932054451ff5583ff094bca6f675df2f8bc1a6e9"


def post_install(self):
    self.install_license("LICENSE")
