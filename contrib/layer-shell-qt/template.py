pkgname = "layer-shell-qt"
pkgver = "6.1.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
pkgdesc = "Qt6 component exposing Wayland wl-layer-shell protocol"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/plasma/layer-shell-qt/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/layer-shell-qt-{pkgver}.tar.xz"
sha256 = "7c60e37301e8f343ef4965494b60186fda82798dd29aadbb35712daf62e34f53"
# FIXME: cfi kills plasmashell (on desktop/panel right click) in libLayerShellQtInterface.so
hardening = ["vis", "!cfi"]


@subpackage("layer-shell-qt-devel")
def _devel(self):
    return self.default_devel()
