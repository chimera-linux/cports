pkgname = "zvm"
pkgver = "0.7.6"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Zig version manager"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/tristanisham/zvm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "463022cdfec76e4a31a47fade9c09477bcd0e775d52b72f44e7b25bc08b44a25"


def post_install(self):
    self.install_license("LICENSE")
