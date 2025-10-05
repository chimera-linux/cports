pkgname = "ov"
pkgver = "0.42.1"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal pager"
license = "MIT"
url = "https://noborus.github.io/ov"
source = f"https://github.com/noborus/ov/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "94a712214125fd6de24f0235e7aa8aa83d9220213036c73065321f2cc9ff2483"


def post_install(self):
    self.install_license("LICENSE")
