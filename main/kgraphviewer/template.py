pkgname = "kgraphviewer"
pkgver = "26.08.0"
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
sha256 = "955dd7c8119015d960dd883ffe66017f766ec5b5f3a0090257e8983c6df8a381"
hardening = ["vis"]


@subpackage("kgraphviewer-devel")
def _(self):
    return self.default_devel()
