pkgname = "python-cloudflare"
pkgver = "3.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = [
    "python-jsonlines",
    "python-pyyaml",
    "python-requests",
]
checkdepends = [
    "python-pytest",
    "python-pytest-asyncio",
    "python-time-machine",
] + depends
pkgdesc = "Python wrapper for the Cloudflare v4 API"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/cloudflare/cloudflare-python"
source = f"$(PYPI_SITE)/c/cloudflare/cloudflare-{pkgver}.tar.gz"
sha256 = "212ead08c8bd9ea1796286bb5d954d157991b3dbcab0c526332f775298ccce9f"
# tests all fail with an upgrade warning or need network
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
