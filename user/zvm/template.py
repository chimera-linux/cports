pkgname = "zvm"
pkgver = "0.7.3"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "174ad7a463e22b2f32101437c5df2832f4e3f1344282f0d5493cc561b6d2a7c8"


def post_install(self):
    self.install_license("LICENSE")
