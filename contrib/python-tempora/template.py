pkgname = "python-tempora"
pkgver = "5.6.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python-jaraco.functools",
    "python-pytz",
]
checkdepends = [
    "python-pytest",
    "python-freezegun",
]
pkgdesc = "Objects and routines pertaining to date and time"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jaraco/tempora"
source = f"$(PYPI_SITE)/t/tempora/tempora-{pkgver}.tar.gz"
sha256 = "3bfcc12cbdbbbafecaaccb9097fc3754435b9d063dce43338e4fa87d39104aed"
# fixtures aren't applied
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
