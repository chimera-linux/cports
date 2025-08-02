pkgname = "python-distlib"
pkgver = "0.4.0"
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
sha256 = "feec40075be03a04501a973d81f633735b4b69f98b05450592310c0f401a4e0d"


def post_install(self):
    self.uninstall("usr/lib/python3*/site-packages/distlib/*.exe", glob=True)
