pkgname = "layer-shell-qt"
pkgver = "6.8.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qglobal_p.h/qwaylanddisplay_p.h etc
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
pkgdesc = "Qt6 component exposing Wayland wl-layer-shell protocol"
license = "GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://kde.org/plasma-desktop"
source = f"$(KDE_SITE)/plasma/{pkgver}/layer-shell-qt-{pkgver}.tar.xz"
sha256 = "8866504834e4727e30ca3674207781dc9a3ac50c8f042bbbc8d8cfdf2ece32a1"
hardening = ["vis"]


@subpackage("layer-shell-qt-devel")
def _(self):
    return self.default_devel()
