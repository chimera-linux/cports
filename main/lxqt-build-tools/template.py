pkgname = "lxqt-build-tools"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "LXQt build and packaging tooling"
license = "BSD-3-Clause"
url = "https://github.com/lxqt/lxqt-build-tools"
source = f"{url}/releases/download/{pkgver}/lxqt-build-tools-{pkgver}.tar.xz"
sha256 = "1214e12ca06561ca724e67092ae1265fdd23128fde449e9d3b0275cb2a051d43"


def post_install(self):
    self.install_license("BSD-3-Clause")
