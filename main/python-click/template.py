pkgname = "python-click"
pkgver = "8.4.2"
pkgrel = 0
build_style = "python_pep517"
# can behave weirdly
make_check_args = ["--deselect", "tests/test_utils.py::test_echo_via_pager"]
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python"]
checkdepends = ["less", "python-pytest"]
pkgdesc = "Python module for command line interfaces"
license = "BSD-3-Clause"
url = "https://palletsprojects.com/p/click"
source = f"$(PYPI_SITE)/c/click/click-{pkgver}.tar.gz"
sha256 = "9a6cea6e60b17ebe0a44c5cc636d94f09bd66142c1cd7d8b4cd731c4917a15f6"


def post_install(self):
    self.install_license("LICENSE.txt")
