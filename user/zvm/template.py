pkgname = "zvm"
pkgver = "0.7.5"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bc3e5406c1de6a20529d98c91738912b118da46ec0df6b3b3224afa579140386"


def post_install(self):
    self.install_license("LICENSE")
