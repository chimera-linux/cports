pkgname = "python-pytest-subtests"
pkgver = "0.12.1"
pkgrel = 1
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
source = f"$(PYPI_SITE)/p/pytest-subtests/pytest-subtests-{pkgver}.tar.gz"
sha256 = "d6605dcb88647e0b7c1889d027f8ef1c17d7a2c60927ebfdc09c7b0d8120476d"


def post_install(self):
    self.install_license("LICENSE")
