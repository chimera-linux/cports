pkgname = "moor"
pkgver = "2.7.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}", "./cmd/moor"]
hostmakedepends = ["go"]
renames = ["moar"]
pkgdesc = "Terminal pager program"
license = "BSD-2-Clause"
url = "https://github.com/walles/moor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c80ef80f4300a9e0d60f76e61fd20b6dc6345ce800005805715d8b95dca4d330"


def install(self):
    self.install_bin("build/moor")
    self.install_license("LICENSE")
    self.install_man("moor.1")
