pkgname = "rofi-rbw"
pkgver = "1.6.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-hatchling", "python-installer"]
makedepends = ["python-configargparse"]
depends = [*makedepends, "rbw"]
pkgdesc = "Rofi frontend for Bitwarden"
license = "MIT"
url = "https://github.com/fdw/rofi-rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4b74b4cca59cdd84efcc6c21cb340e4d80748d96433458ebd979966f40ea7dd3"
# No tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("docs/rofi-rbw.1")
