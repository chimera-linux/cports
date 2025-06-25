pkgname = "python-pytest-subtests"
pkgver = "0.14.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python-attrs", "python-pytest"]
checkdepends = ["python-pytest-xdist", *depends]
pkgdesc = "Unittest subTest() and subtests fixture"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-subtests"
source = f"$(PYPI_SITE)/p/pytest-subtests/pytest_subtests-{pkgver}.tar.gz"
sha256 = "7154a8665fd528ee70a76d00216a44d139dc3c9c83521a0f779f7b0ad4f800de"


def post_install(self):
    self.install_license("LICENSE")
