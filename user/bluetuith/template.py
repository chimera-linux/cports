pkgname = "bluetuith"
pkgver = "0.2.7"
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
sha256 = "9586383c1703dd4e12e81f5f68e5144481aed8fb0526ee046dc3a80558d0f0dc"


def post_install(self):
    self.install_license("LICENSE")
