pkgname = "layer-shell-qt"
pkgver = "6.7.5"
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
sha256 = "ccdcfec7081ca956f7a52c9113a4df3a226575bfbe98b56a2a9a4d7d7e19e8f0"
hardening = ["vis"]


@subpackage("layer-shell-qt-devel")
def _(self):
    return self.default_devel()
