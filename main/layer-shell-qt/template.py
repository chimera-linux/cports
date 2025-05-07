pkgname = "layer-shell-qt"
pkgver = "6.3.5"
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
url = "https://api.kde.org/plasma/layer-shell-qt/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/layer-shell-qt-{pkgver}.tar.xz"
sha256 = "7062ca0e50dcce97dd11d8adf1b86d49f1c56423f2341dceb3ea40dc48206e25"
hardening = ["vis"]


@subpackage("layer-shell-qt-devel")
def _(self):
    return self.default_devel()
