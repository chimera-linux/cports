pkgname = "python-pytest-subtests"
pkgver = "0.14.0"
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
sha256 = "8849818a0a515e8052734888cd0f6701291fdbf77552664d9ac772a2f8cc8f0f"


def post_install(self):
    self.install_license("LICENSE")
