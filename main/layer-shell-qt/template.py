pkgname = "layer-shell-qt"
pkgver = "6.3.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/plasma/layer-shell-qt/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/layer-shell-qt-{pkgver}.tar.xz"
sha256 = "8e19ea265cbba4b010e2d4997140e0c9a0bbb5a11b50accc8bd4338e7af7e97f"
hardening = ["vis"]


@subpackage("layer-shell-qt-devel")
def _(self):
    return self.default_devel()
