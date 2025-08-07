pkgname = "zvm"
pkgver = "0.8.7"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c12bbd44881eeb14009a6ce2d435793c70046c4502a5666229e972804a9bf1ea"


def post_install(self):
    self.install_license("LICENSE")
