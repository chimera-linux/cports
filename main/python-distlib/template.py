pkgname = "python-distlib"
pkgver = "0.3.9"
pkgrel = 0
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
sha256 = "a60f20dea646b8a33f3e7772f74dc0b2d0772d2837ee1342a00645c81edf9403"


def post_install(self):
    self.uninstall("usr/lib/python3*/site-packages/distlib/*.exe", glob=True)
