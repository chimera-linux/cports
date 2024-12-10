pkgname = "python-pytest-subtests"
pkgver = "0.14.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-attrs", "python-pytest"]
checkdepends = ["python-pytest-xdist", *depends]
pkgdesc = "Unittest subTest() and subtests fixture"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-subtests"
source = f"$(PYPI_SITE)/p/pytest-subtests/pytest_subtests-{pkgver}.tar.gz"
sha256 = "350c00adc36c3aff676a66135c81aed9e2182e15f6c3ec8721366918bbbf7580"


def post_install(self):
    self.install_license("LICENSE")
