pkgname = "kgraphviewer"
pkgver = "25.04.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "graphviz-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kparts-devel",
    "kwidgetsaddons-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
# dot
depends = ["graphviz"]
pkgdesc = "Graphviz DOT file viewer"
license = "GPL-2.0-only"
url = "https://invent.kde.org/graphics/kgraphviewer"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kgraphviewer-{pkgver}.tar.xz"
)
sha256 = "484bf8132a1ecbec0a9fcf05274bb08081e6d288882a9835e86cb3177a7742bf"
hardening = ["vis"]


@subpackage("kgraphviewer-devel")
def _(self):
    return self.default_devel()
