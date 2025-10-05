pkgname = "bluetuith"
pkgver = "0.2.3"
pkgrel = 13
build_style = "go"
hostmakedepends = ["go"]
depends = ["bluez"]
pkgdesc = "TUI bluetooth manager"
license = "MIT"
url = "https://github.com/darkhz/bluetuith"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ff4ca6e5fda87b33c472b703c81b4000d1df4efb2bdc0af1762e4a3e3c507228"


def post_install(self):
    self.install_license("LICENSE")
