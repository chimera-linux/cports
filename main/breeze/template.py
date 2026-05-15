pkgname = "breeze"
pkgver = "6.6.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_QT5=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "frameworkintegration-devel",
    "kcmutils-devel",
    "kcolorscheme-devel",
    "kcoreaddons-devel",
    "kdecoration-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kirigami-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
depends = [
    "breeze-icons",
    "frameworkintegration",
    self.with_pkgver("breeze-cursors"),
]
pkgdesc = "Breeze visual style for the KDE Plasma Desktop"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/breeze"
source = f"$(KDE_SITE)/plasma/{pkgver}/breeze-{pkgver}.tar.xz"
sha256 = "06c4c3e466cd03a8c1e411a38b04756b6e145879a560534b2fc44666d41330f4"
hardening = ["vis"]
# TODO: split qt6 theme?


@subpackage("breeze-cursors")
def _(self):
    self.subdesc = "cursor themes"
    return [
        "usr/share/icons/breeze_cursors",
        "usr/share/icons/Breeze_Light",
    ]


@subpackage("breeze-devel")
def _(self):
    return self.default_devel()
