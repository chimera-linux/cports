pkgname = "ov"
pkgver = "0.42.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal pager"
license = "MIT"
url = "https://noborus.github.io/ov"
source = f"https://github.com/noborus/ov/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0532e0ca807dfcf6d77837117f90861051ab7cbecac9c6aa815294223cd1444c"


def post_install(self):
    self.install_license("LICENSE")
