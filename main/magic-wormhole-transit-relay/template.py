pkgname = "magic-wormhole-transit-relay"
pkgver = "0.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-autobahn", "python-twisted"]
checkdepends = ["python-mock", "python-pytest", *depends]
pkgdesc = "Transit relay server for Magic Wormhole"
license = "MIT"
url = "https://github.com/magic-wormhole/magic-wormhole-transit-relay"
source = f"$(PYPI_SITE)/m/magic-wormhole-transit-relay/magic_wormhole_transit_relay-{pkgver}.tar.gz"
sha256 = "a2c2e777cafcd843a2f22f0a4b3c3bd3cae85cc2303fead1646d1763ad6d1a4a"


def post_install(self):
    self.install_license("LICENSE")
