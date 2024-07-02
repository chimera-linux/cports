pkgname = "bluetuith"
pkgver = "0.2.2"
pkgrel = 3
build_style = "go"
hostmakedepends = ["go"]
depends = ["bluez"]
pkgdesc = "TUI bluetooth manager"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/darkhz/bluetuith"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2a02f51c53668fa3171e642e25f268fc50fbb2438f764956fb7cd46fb786083d"
# objcopy ppc64le fails
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")
