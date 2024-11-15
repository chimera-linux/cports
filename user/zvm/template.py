pkgname = "zvm"
pkgver = "0.8.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9f822942e125159176d25f742bf11e8af2827ba7840d9f3f8db9491451a9722f"


def post_install(self):
    self.install_license("LICENSE")
