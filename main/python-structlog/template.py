pkgname = "python-structlog"
pkgver = "25.3.0"
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
sha256 = "8dab497e6f6ca962abad0c283c46744185e0c9ba900db52a423cb6db99f7abeb"


def post_install(self):
    self.install_license("LICENSE-MIT")
