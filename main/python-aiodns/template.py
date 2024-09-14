pkgname = "python-aiodns"
pkgver = "3.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-pycares"]
pkgdesc = "Simple DNS resolver for asyncio"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/saghul/aiodns"
source = f"$(PYPI_SITE)/a/aiodns/aiodns-{pkgver}.tar.gz"
sha256 = "62869b23409349c21b072883ec8998316b234c9a9e36675756e8e317e8768f72"
# no standard pytest tests, requires an internet connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
