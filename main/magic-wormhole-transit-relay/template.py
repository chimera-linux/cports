pkgname = "magic-wormhole-transit-relay"
pkgver = "0.3.1"
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
sha256 = "2ef2efbe4d34f0e624870f842259fd733ba77152ed310af4349774a62884900e"


def post_install(self):
    self.install_license("LICENSE")
