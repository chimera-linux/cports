pkgname = "python-pexpect"
pkgver = "4.9.0"
pkgrel = 1
build_style = "python_pep517"
# FIXME: some test in this can hang on ppc64le
make_check_args = ["--deselect", "tests/test_socket.py"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-ptyprocess"]
checkdepends = [
    "bash",
    "mandoc",
    "python-pytest",
    "zsh",
    *depends,
]
pkgdesc = "Python port of expect(1) for child process handling"
license = "ISC"
url = "https://pexpect.readthedocs.io/en/stable"
source = f"$(PYPI_SITE)/p/pexpect/pexpect-{pkgver}.tar.gz"
sha256 = "ee7d41123f3c9911050ea2c2dac107568dc43b2d3b0c7557a33212c398ead30f"


def post_extract(self):
    # can't deal with escapes
    self.rm("tests/test_replwrap.py")


def post_install(self):
    self.install_license("LICENSE")
