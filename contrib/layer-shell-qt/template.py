pkgname = "layer-shell-qt"
pkgver = "6.1.3"
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
sha256 = "a201bd3c867130e96cae75dcfec07f82af74dc2e8074d8d1bd9b0ae2645bf802"
# CFI: kills plasmashell (on desktop/panel right click) in libLayerShellQtInterface.so
hardening = ["vis", "!cfi"]


@subpackage("layer-shell-qt-devel")
def _devel(self):
    return self.default_devel()
