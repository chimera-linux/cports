pkgname = "rofi-rbw"
pkgver = "1.6.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-hatchling", "python-installer"]
makedepends = ["python-configargparse"]
depends = [*makedepends, "rbw"]
pkgdesc = "Rofi frontend for Bitwarden"
license = "MIT"
url = "https://github.com/fdw/rofi-rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "32e9b93fe7b1e69dc69490f14d0a87bf41eca39ae03ef8cc9cdfd35d89346f3e"
# No tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("docs/rofi-rbw.1")
