pkgname = "bluetuith"
pkgver = "0.2.5"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
depends = ["bluez"]
pkgdesc = "TUI bluetooth manager"
license = "MIT"
url = "https://github.com/darkhz/bluetuith"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9e48728843d1e50c8199e532a714c989681f7ab041fb64a7cb093530383e86b0"


def post_install(self):
    self.install_license("LICENSE")
