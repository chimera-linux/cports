pkgname = "python-structlog"
pkgver = "24.4.0"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "Apache-2.0 OR MIT"
url = "https://structlog.org"
source = f"$(PYPI_SITE)/s/structlog/structlog-{pkgver}.tar.gz"
sha256 = "b27bfecede327a6d2da5fbc96bd859f114ecc398a6389d664f62085ee7ae6fc4"


def post_install(self):
    self.install_license("LICENSE-MIT")
