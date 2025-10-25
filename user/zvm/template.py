pkgname = "zvm"
pkgver = "0.8.10"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "96d46c820cd2624b78ccbe49217e56c9c4e3a4242c4f9102fe5c59165777c9a3"


def post_install(self):
    self.install_license("LICENSE")
