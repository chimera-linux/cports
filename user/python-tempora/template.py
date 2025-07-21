pkgname = "python-tempora"
pkgver = "5.8.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-dateutil",
    "python-jaraco.functools",
    "python-pytz",
]
checkdepends = [
    "python-freezegun",
    "python-pytest",
]
pkgdesc = "Objects and routines pertaining to date and time"
license = "MIT"
url = "https://github.com/jaraco/tempora"
source = f"$(PYPI_SITE)/t/tempora/tempora-{pkgver}.tar.gz"
sha256 = "1e9606e65a3f2063460961d68515dee07bdaca0859305a8d3e6604168175fef1"
# fixtures aren't applied
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
