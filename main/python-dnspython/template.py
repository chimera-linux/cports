pkgname = "python-dnspython"
pkgver = "2.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "DNS toolkit for Python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "ISC"
url = "https://www.dnspython.org"
source = f"$(PYPI_SITE)/d/dnspython/dnspython-{pkgver}.tar.gz"
sha256 = "ce9c432eda0dc91cf618a5cedf1a4e142651196bbcd2c80e89ed5a907e5cfaf1"


def post_install(self):
    self.install_license("LICENSE")
