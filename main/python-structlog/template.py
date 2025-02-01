pkgname = "python-structlog"
pkgver = "25.1.0"
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
sha256 = "2ef2a572e0e27f09664965d31a576afe64e46ac6084ef5cec3c2b8cd6e4e3ad3"


def post_install(self):
    self.install_license("LICENSE-MIT")
