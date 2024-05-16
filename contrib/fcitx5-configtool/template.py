pkgname = "fcitx5-configtool"
pkgver = "5.1.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=OFF",
    # TODO: KDE native configurator
    "-DENABLE_KCM=OFF",
    "-DENABLE_TEST=ON",
    "-DUSE_QT6=ON",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "iso-codes",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
    "wayland-progs",
]
makedepends = [
    "fcitx5-devel",
    "fcitx5-qt-devel",
    "kitemviews-devel",
    "kwidgetsaddons-devel",
    "libxkbcommon-devel",
    "libxkbfile-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "xkeyboard-config",
]
depends = ["qt6-qtsvg"]
pkgdesc = "Configuration tool for Fcitx5"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://fcitx-im.org"
source = f"https://github.com/fcitx/fcitx5-configtool/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "26d949116915e870f345171d24a052cda301628e8f6cf4ee62fac2a3baebd101"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]
