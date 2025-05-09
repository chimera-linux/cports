pkgname = "kdegraphics-mobipocket"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kio-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE plugins for mobipocket files"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/graphics/kdegraphics-mobipocket"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdegraphics-mobipocket-{pkgver}.tar.xz"
sha256 = "e742b6a69099aea27807c0c856e161b2bd9859e8745cbb09ac51cb4dfd8d7bf9"
hardening = ["vis"]


@subpackage("kdegraphics-mobipocket-devel")
def _(self):
    return self.default_devel()
