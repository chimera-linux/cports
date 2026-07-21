pkgname = "fcitx5-qt"
pkgver = "5.1.14"
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
    "pkgconf",
    "qt6-qtbase",
    "wayland-progs",
]
makedepends = [
    "fcitx5-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "qt6-qtbase-private-devel",  # qguiapplication_p.h
    "qt6-qtwayland-devel",
]
pkgdesc = "Qt library and IM module for Fcitx5"
license = "BSD-3-Clause AND LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = f"https://github.com/fcitx/fcitx5-qt/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "80cbbc6b3ad08a6b7a40bb6cc4072e1c3bcf2099a821ce04b1bd510848c804d7"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("fcitx5-qt-devel")
def _(self):
    return self.default_devel()
