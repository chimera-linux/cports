pkgname = "zvm"
pkgver = "0.8.6"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a9fd200a497bc6d3a3fe987e864635dd3a8226b75cc25a219451c399ae74318b"


def post_install(self):
    self.install_license("LICENSE")
