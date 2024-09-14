pkgname = "python-authres"
pkgver = "1.2.0"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Authentication-Results verification module"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://launchpad.net/authentication-results-python"
source = f"$(PYPI_SITE)/a/authres/authres-{pkgver}.tar.gz"
sha256 = "93d1b995ad7ce21e62db649f361048125dd6022563a0ae8a23909465f1fd25b7"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
