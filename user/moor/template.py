pkgname = "moor"
pkgver = "2.10.1"
pkgrel = 1
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}", "./cmd/moor"]
hostmakedepends = ["go"]
renames = ["moar"]
pkgdesc = "Terminal pager program"
license = "BSD-2-Clause"
url = "https://github.com/walles/moor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "389a1454ce7deedc43d9a17bce48d044ff6a71ac8ef497ea3e347f3f6bfe3d63"


def install(self):
    self.install_bin("build/moor")
    self.install_license("LICENSE")
    self.install_man("moor.1")
