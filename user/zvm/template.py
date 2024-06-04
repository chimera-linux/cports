pkgname = "zvm"
pkgver = "0.7.1"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c2ebb8943e115d95afa6fa3ed96cddc42658d713e9166254d4d2cd8fa54646d1"


def post_install(self):
    self.install_license("LICENSE")
