pkgname = "rofimoji"
pkgver = "6.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-hatchling", "python-installer"]
makedepends = ["python-configargparse"]
depends = [*makedepends]
pkgdesc = "Emoji, unicode and general character picker"
license = "MIT"
url = "https://github.com/fdw/rofimoji"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "721dd1f6a20ea4a236a1316b1a996ab9b235dfecced31ffd6c8a88c815d57cfb"
# No tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
