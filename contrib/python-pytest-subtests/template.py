pkgname = "python-pytest-subtests"
pkgver = "0.11.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = [
    "python-attrs",
    "python-pytest",
]
pkgdesc = "Unittest subTest() and subtests fixture"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-subtests"
source = f"$(PYPI_SITE)/p/pytest-subtests/pytest-subtests-{pkgver}.tar.gz"
sha256 = "51865c88457545f51fb72011942f0a3c6901ee9e24cbfb6d1b9dc1348bafbe37"


def post_install(self):
    self.install_license("LICENSE")
