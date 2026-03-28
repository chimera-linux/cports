pkgname = "rofimoji"
pkgver = "6.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-hatchling", "python-installer"]
makedepends = ["python-configargparse"]
depends = [*makedepends]
pkgdesc = "Emoji, unicode and general character picker"
license = "MIT"
url = "https://github.com/fdw/rofimoji"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9b537d8936a4e4092bbf6cfdc66ba8908b7300a3027ee44c49930199f3674dc3"
# No tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
