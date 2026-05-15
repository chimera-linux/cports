pkgname = "copyq"
pkgver = "15.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_NATIVE_NOTIFICATIONS=OFF",
    "-DWITH_AUDIO=OFF",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kguiaddons-devel",
    "libxfixes-devel",
    "libxtst-devel",
    "qca-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qtkeychain-devel",
]
pkgdesc = "Clipboard manager with advanced features"
license = "GPL-3.0-or-later"
url = "https://hluk.github.io/CopyQ"
source = f"https://github.com/hluk/CopyQ/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "19665e503997e9d2ffd6f062df43255ee2be38d888d8cc22215474196016bb39"
# CFI: loading plugins fail with cfi enabled
hardening = ["vis", "!cfi"]
# requires building project a second time in debug mode
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
