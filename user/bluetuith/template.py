pkgname = "bluetuith"
pkgver = "0.2.6"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/darkhz/bluetuith/cmd.Version={pkgver}"
]
hostmakedepends = ["go"]
depends = ["bluez"]
pkgdesc = "TUI bluetooth manager"
license = "MIT"
url = "https://github.com/darkhz/bluetuith"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7e4e83fc0ed34b7ffa7d6035363c5380adfb4116136354e32149beb9dcb50bc9"


def post_install(self):
    self.install_license("LICENSE")
