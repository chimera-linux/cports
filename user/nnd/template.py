pkgname = "nnd"
pkgver = "0.80"
pkgrel = 0
archs = ["x86_64"]
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = []
pkgdesc = "TUI-Debugger for linux"
license = "Apache-2.0"
url = "https://github.com/al13n321/nnd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "034e06697f06a7507f22e0433d55a8e687c9028bb229efc2c32f3f36c5925eae"


def post_install(self):
    self.install_license("LICENSE")
