pkgname = "ov"
pkgver = "0.45.1"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Terminal pager"
license = "MIT"
url = "https://noborus.github.io/ov"
source = f"https://github.com/noborus/ov/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dc1fef378297f3bc57f4fcd2a502f389bdcaf4266601a1a3eb790e74f98542a5"


def post_install(self):
    self.install_license("LICENSE")
