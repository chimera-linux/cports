pkgname = "bluetui"
pkgver = "0.8.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["bluez"]
pkgdesc = "TUI for managing bluetooth devices"
license = "GPL-3.0-only"
url = "https://github.com/pythops/bluetui"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9b82b3c268a20bf04e55095cacc3341d46013ccfa7d268c4f225d4a88f9c7138"


def post_install(self):
    self.install_license("LICENSE")
