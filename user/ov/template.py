pkgname = "ov"
pkgver = "0.44.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal pager"
license = "MIT"
url = "https://noborus.github.io/ov"
source = f"https://github.com/noborus/ov/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "87ee2f7d6477b02b5562d0da033e7a8f4f49c92fe7637c47985646c685474984"


def post_install(self):
    self.install_license("LICENSE")
