pkgname = "bluetuith"
pkgver = "0.2.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
depends = ["bluez"]
pkgdesc = "TUI bluetooth manager"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/darkhz/bluetuith"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "34b853a2e1ef1c77d06dc761c5e40050763d509cadc98a48e5342154633fffde"
# objcopy ppc64le fails
options = ["!debug"]


def post_install(self):
    self.install_license("LICENSE")
