pkgname = "layer-shell-qt"
pkgver = "6.7.91"
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/layer-shell-qt-{pkgver}.tar.xz"
sha256 = "88327752a00e70fcd55ffded429f13840c0f6368698651a73b9e92f8cc4ff3c9"
hardening = ["vis"]


@subpackage("layer-shell-qt-devel")
def _(self):
    return self.default_devel()
