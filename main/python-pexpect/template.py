pkgname = "python-pexpect"
pkgver = "4.9.0"
pkgrel = 0
build_style = "python_pep517"
# we don't have zsh in main/
make_check_args = [
    "--deselect=tests/test_replwrap.py::REPLWrapTestCase::test_zsh"
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-ptyprocess"]
checkdepends = ["bash", "mandoc", "python-pytest"] + depends
pkgdesc = "Allows easy control of interactive console applications"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "ISC"
url = "https://github.com/pexpect/pexpect"
source = f"$(PYPI_SITE)/p/pexpect/pexpect-{pkgver}.tar.gz"
sha256 = "ee7d41123f3c9911050ea2c2dac107568dc43b2d3b0c7557a33212c398ead30f"


def post_install(self):
    self.install_license("LICENSE")
