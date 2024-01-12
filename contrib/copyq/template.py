pkgname = "copyq"
pkgver = "7.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DWITH_QT6=ON"]
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
sha256 = "ce0265b0a86350fda7bfa1a9d4b74d794a4077551b28186012683567d6fd8158"
# FIXME: segfaults with cfi
hardening = ["vis", "!cfi"]
# requires building project a second time in debug mode
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
