pkgname = "kgraphviewer"
pkgver = "25.12.0"
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
sha256 = "c26ab2f1c63f30ef909bf62dd3f87882947e243256b53c01dc7d4142c70538f6"
hardening = ["vis"]


@subpackage("kgraphviewer-devel")
def _(self):
    return self.default_devel()
