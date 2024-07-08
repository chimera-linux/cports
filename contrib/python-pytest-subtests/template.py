pkgname = "python-pytest-subtests"
pkgver = "0.13.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-attrs", "python-pytest"]
checkdepends = ["python-pytest-xdist"] + depends
pkgdesc = "Unittest subTest() and subtests fixture"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-subtests"
source = f"$(PYPI_SITE)/p/pytest-subtests/pytest_subtests-{pkgver}.tar.gz"
sha256 = "9e02b9d243c0379b02abf3e0887da122bcb2714b021c3608a37f17ce210adce5"


def post_install(self):
    self.install_license("LICENSE")
