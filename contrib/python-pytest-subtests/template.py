pkgname = "python-pytest-subtests"
pkgver = "0.13.1"
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
sha256 = "989e38f0f1c01bc7c6b2e04db7d9fd859db35d77c2c1a430c831a70cbf3fde2d"


def post_install(self):
    self.install_license("LICENSE")
