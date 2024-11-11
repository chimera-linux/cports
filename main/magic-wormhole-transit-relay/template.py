pkgname = "magic-wormhole-transit-relay"
pkgver = "0.4.0"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/magic-wormhole/magic-wormhole-transit-relay"
source = f"$(PYPI_SITE)/m/magic-wormhole-transit-relay/magic-wormhole-transit-relay-{pkgver}.tar.gz"
sha256 = "912d835da21b11266c77111dc9b5e5800263fc0b98f0a179962267df41819e8c"


def post_install(self):
    self.install_license("LICENSE")
