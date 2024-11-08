pkgname = "lxqt-build-tools"
pkgver = "2.1.0"
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
sha256 = "2458b629936f5e1ff8850e9953e49d66b96ac419cb484fed0a4d28a711fd8ef9"


def post_install(self):
    self.install_license("BSD-3-Clause")
