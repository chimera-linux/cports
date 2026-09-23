pkgname = "ov"
pkgver = "0.54.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal pager"
license = "MIT"
url = "https://noborus.github.io/ov"
source = f"https://github.com/noborus/ov/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "78248f48adb5deb6ca2e560b57583f0ae66ac5e71704b7dc0b35d2378e0df5ac"


def post_install(self):
    self.install_license("LICENSE")
