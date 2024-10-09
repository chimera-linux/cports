pkgname = "fcitx5-configtool"
pkgver = "5.1.7"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=OFF",
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
    "kcmutils-devel",
    "kcoreaddons-devel",
    "kdeclarative-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kirigami-devel",
    "kitemviews-devel",
    "kpackage-devel",
    "ksvg-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "libxkbcommon-devel",
    "libxkbfile-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "xkeyboard-config",
]
depends = [
    "qt6-qtsvg",
]
pkgdesc = "Configuration tool for Fcitx5"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://fcitx-im.org"
source = f"https://github.com/fcitx/fcitx5-configtool/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c134b082ea9cab0102b9427f39a3714f4a71146ac082e4e6c7c18e4b8dd2aaa7"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]


@subpackage("fcitx5-configtool-kde")
def _(self):
    self.subdesc = "KCM integration"
    self.depends += [self.parent]

    return [
        "usr/bin/fcitx5-plasma-theme-generator",
        "usr/share/applications/kcm_fcitx5.desktop",
        "usr/share/locale/*/*/kcm*",
    ]
