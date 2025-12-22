pkgname = "moor"
pkgver = "2.9.6"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}", "./cmd/moor"]
hostmakedepends = ["go"]
renames = ["moar"]
pkgdesc = "Terminal pager program"
license = "BSD-2-Clause"
url = "https://github.com/walles/moor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "86b58a81f1ca10ee2873c3618c4effe447fa76bc4c89eaa1f0dce1d32dadff9d"


def install(self):
    self.install_bin("build/moor")
    self.install_license("LICENSE")
    self.install_man("moor.1")
