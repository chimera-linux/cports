pkgname = "fcitx5-qt"
pkgver = "5.1.7"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_QT4=OFF",
    "-DENABLE_QT5=OFF",
    "-DENABLE_QT6=ON",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "qt6-qtbase",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "fcitx5-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qtwayland-devel",
]
pkgdesc = "Qt library and IM module for Fcitx5"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause AND LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = f"https://github.com/fcitx/fcitx5-qt/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "586e35e70e656ce387d7c87b58af1294599bd10385f983580235a2efeca666ee"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("fcitx5-qt-devel")
def _(self):
    return self.default_devel()
