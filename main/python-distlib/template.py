pkgname = "python-distlib"
pkgver = "0.4.3"
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
license = "PSF-2.0"
url = "https://github.com/vsajip/distlib"
source = f"$(PYPI_SITE)/d/distlib/distlib-{pkgver}.tar.gz"
sha256 = "f152097224a0ae24be5a0f6bae1b9359af82133bce63f98a95f86cae1aede9ed"


def post_install(self):
    self.uninstall("usr/lib/python3*/site-packages/distlib/*.exe", glob=True)
