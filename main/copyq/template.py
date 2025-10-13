pkgname = "copyq"
pkgver = "12.0.1"
pkgrel = 0
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
    "libxfixes-devel",
    "libxtst-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
]
pkgdesc = "Clipboard manager with advanced features"
license = "GPL-3.0-or-later"
url = "https://hluk.github.io/CopyQ"
source = f"https://github.com/hluk/CopyQ/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "452cd2acbe9d70e0b93bef413620dfece363f0595b19788d71035c8455d6097f"
# CFI: loading plugins fail with cfi enabled
hardening = ["vis", "!cfi"]
# requires building project a second time in debug mode
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
