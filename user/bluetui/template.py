pkgname = "bluetui"
pkgver = "0.8.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["bluez"]
pkgdesc = "TUI for managing bluetooth devices"
license = "GPL-3.0-only"
url = "https://github.com/pythops/bluetui"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "16b5c108f7f02cb6578e5bda5eb9cf7d1e1552b2c53d88533a7e4f5e9f12969d"


def post_install(self):
    self.install_license("LICENSE")
