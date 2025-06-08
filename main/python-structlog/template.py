pkgname = "python-structlog"
pkgver = "25.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = [
    "python-freezegun",
    "python-pretend",
    "python-pytest-asyncio",
    "python-simplejson",
]
pkgdesc = "Python logging library"
license = "Apache-2.0 OR MIT"
url = "https://structlog.org"
source = f"$(PYPI_SITE)/s/structlog/structlog-{pkgver}.tar.gz"
sha256 = "186cd1b0a8ae762e29417095664adf1d6a31702160a46dacb7796ea82f7409e4"


def post_install(self):
    self.install_license("LICENSE-MIT")
