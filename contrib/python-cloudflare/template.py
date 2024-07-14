pkgname = "python-cloudflare"
pkgver = "2.20.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-jsonlines",
    "python-pyyaml",
    "python-requests",
]
checkdepends = [
    "python-pytest",
    "python-pytz",
    *depends,
]
pkgdesc = "Python wrapper for the Cloudflare v4 API"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/cloudflare/python-cloudflare"
source = f"$(PYPI_SITE)/c/cloudflare/cloudflare-{pkgver}.tar.gz"
sha256 = "46aefc39dfaa2365d639b423cec2cd5350ae11153c7247d3eb3545bdcf01a68a"
# tests all fail with an upgrade warning or need network
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
