pkgname = "ab-av1"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cargo"
makedepends = ["cargo"]
depends = ["ffmpeg"]
pkgdesc = "AV1 re-encoding using ffmpeg, svt-av1, XPSNR and VMAF"
maintainer = "LeFantome <fantome137@proton.me>"
license = "MIT"
url = "https://github.com/alexheretic/ab-av1"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "093b06ff2e884372a2a145c3bba824f60df18f6f2c7cd5037f1152adbf1976e3"


def post_install(self):
    self.install_license("LICENSE")
