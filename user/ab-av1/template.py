pkgname = "ab-av1"
pkgver = "0.8.0"
pkgrel = 0
build_style = "cargo"
makedepends = ["cargo"]
depends = ["ffmpeg"]
pkgdesc = "AV1 re-encoding using ffmpeg, svt-av1 and vmaf"
maintainer = "LeFantome <fantome137@proton.me>"
license = "MIT"
url = "https://github.com/alexheretic/ab-av1"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "38886629888aba806e6ab5f560cc424ebfa4ee1b652780b59638e11219ebf843"


def post_install(self):
    self.install_license("LICENSE")
