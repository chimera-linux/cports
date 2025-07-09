pkgname = "python-tornado"
pkgver = "6.5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python3 web framework and asynchronous networking library"
license = "Apache-2.0"
url = "https://www.tornadoweb.org"
source = f"$(PYPI_SITE)/t/tornado/tornado-{pkgver}.tar.gz"
sha256 = "84ceece391e8eb9b2b95578db65e920d2a61070260594819589609ba9bc6308c"


def post_install(self):
    self.install_license("LICENSE")


def init_check(self):
    self.make_check_args = [
        "--ignore=tornado/test/iostream_test.py",
    ]
