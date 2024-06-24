pkgname = "lxqt-build-tools"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "LXQt build and packaging tooling"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/lxqt/lxqt-build-tools"
source = f"{url}/releases/download/{pkgver}/lxqt-build-tools-{pkgver}.tar.xz"
sha256 = "4599c47d1db35e0bb91e62b672e3fb7eb2ec1fb4dafcab94599b0156f54e7f07"


def post_install(self):
    self.install_license("BSD-3-Clause")
