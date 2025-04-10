pkgname = "python-structlog"
pkgver = "25.2.0"
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
sha256 = "d9f9776944207d1035b8b26072b9b140c63702fd7aa57c2f85d28ab701bd8e92"


def post_install(self):
    self.install_license("LICENSE-MIT")
