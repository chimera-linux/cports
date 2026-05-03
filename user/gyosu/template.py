pkgname = "gyosu"
pkgver = "0.2.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Simple C documentation generator"
license = "AGPL-3.0-only"
url = "https://codeberg.org/emersion/gyosu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0f4f41fc30ac56f2f0204001c988cb4739dcbf53aba890bdb500a0c8b77b8e7c"


def post_install(self):
    self.install_license("LICENSE")
