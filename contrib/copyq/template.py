pkgname = "copyq"
pkgver = "9.0.0"
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
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
]
pkgdesc = "Clipboard manager with advanced features"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://hluk.github.io/CopyQ"
source = f"https://github.com/hluk/CopyQ/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6f8cce371cda8edb87e2a8d2f9de27022720b7b8fae51f67ee7d69b73526f432"
# CFI: loading plugins fail with cfi enabled
hardening = ["vis", "!cfi"]
# requires building project a second time in debug mode
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
