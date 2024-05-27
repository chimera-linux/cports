pkgname = "fcitx5-configtool"
pkgver = "5.1.5"
pkgrel = 1
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
sha256 = "26d949116915e870f345171d24a052cda301628e8f6cf4ee62fac2a3baebd101"
hardening = ["vis", "cfi"]
# fails
options = ["!cross"]


@subpackage("fcitx5-configtool-kde")
def _kde(self):
    self.pkgdesc = f"{pkgdesc} (KCM integration)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"fcitx5-configtool-kde-meta={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/fcitx5-plasma-theme-generator",
        "usr/share/applications/kcm_fcitx5.desktop",
        "usr/share/locale/*/*/kcm*",
    ]


@subpackage("fcitx5-configtool-kde-meta")
def _kde_meta(self):
    self.pkgdesc = f"{pkgdesc} (KDE recommends package)"
    self.options = ["empty"]
    return []
