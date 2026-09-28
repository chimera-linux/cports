pkgname = "lxqt-build-tools"
pkgver = "2.4.0"
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
sha256 = "14999ff954e820a23af44389b9f7c65f9e58b2f1c0a559f0badd38f9b459aee6"


def post_install(self):
    self.install_license("BSD-3-Clause")
