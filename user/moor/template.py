pkgname = "moor"
pkgver = "2.5.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.versionString=v{pkgver}", "./cmd/moor"]
hostmakedepends = ["go"]
renames = ["moar"]
pkgdesc = "Terminal pager program"
license = "BSD-2-Clause"
url = "https://github.com/walles/moor"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1255f622811554d81c285deeeb9de5b4eef867014ebef55d7c076b6dfaf8c00e"


def install(self):
    self.install_bin("build/moor")
    self.install_license("LICENSE")
    self.install_man("moor.1")
