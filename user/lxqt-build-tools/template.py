pkgname = "lxqt-build-tools"
pkgver = "2.5.0"
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
sha256 = "eeeeb7dbc2271238306139e660acabe4124b3ebab5434e1e40b1f08cf5bcd4ce"


def post_install(self):
    self.install_license("BSD-3-Clause")
