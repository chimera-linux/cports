pkgname = "lxqt-build-tools"
pkgver = "2.2.1"
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
sha256 = "13dcdf2e6b55cc334ac0ddadd0c131d46c46e06fab0d6ca7b8b96c260c8e332f"


def post_install(self):
    self.install_license("BSD-3-Clause")
