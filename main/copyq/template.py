pkgname = "copyq"
pkgver = "13.0.0"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DWITH_NATIVE_NOTIFICATIONS=OFF",
    "-DWITH_QT6=ON",
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
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Clipboard manager with advanced features"
license = "GPL-3.0-or-later"
url = "https://hluk.github.io/CopyQ"
source = f"https://github.com/hluk/CopyQ/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c7e0c9aa95b5653dee547f168d58cf5aae4f66ad5f94856a61741ebe9527ad72"
# CFI: loading plugins fail with cfi enabled
hardening = ["vis", "!cfi"]
# requires building project a second time in debug mode
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
