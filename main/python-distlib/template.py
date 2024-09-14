pkgname = "python-distlib"
pkgver = "0.3.8"
pkgrel = 1
build_style = "python_pep517"
make_check_args = [
    "--deselect=tests/test_locators.py::LocatorTestCase",
    "--deselect=tests/test_util.py::UtilTestCase",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Functions for packaging and distribution of Python software"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "PSF-2.0"
url = "https://github.com/vsajip/distlib"
source = f"$(PYPI_SITE)/d/distlib/distlib-{pkgver}.tar.gz"
sha256 = "1530ea13e350031b6312d8580ddb6b27a104275a31106523b8f123787f494f64"


def post_install(self):
    self.uninstall("usr/lib/python3*/site-packages/distlib/*.exe", glob=True)
