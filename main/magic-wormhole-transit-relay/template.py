pkgname = "magic-wormhole-transit-relay"
pkgver = "0.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-twisted"]
checkdepends = ["python-mock", "python-pytest", *depends]
pkgdesc = "Transit relay server for Magic Wormhole"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/magic-wormhole/magic-wormhole-transit-relay"
source = f"$(PYPI_SITE)/m/magic-wormhole-transit-relay/magic-wormhole-transit-relay-{pkgver}.tar.gz"
sha256 = "cb4801b46890eaff97286e0e3fec62d1d52ffe317d140083b6336a1fb4e8fa5e"


def post_install(self):
    self.install_license("LICENSE")
