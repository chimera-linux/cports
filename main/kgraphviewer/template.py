pkgname = "kgraphviewer"
pkgver = "24.08.1"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://invent.kde.org/graphics/kgraphviewer"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kgraphviewer-{pkgver}.tar.xz"
)
sha256 = "35d46abf16e52d064a240e94690e0789719c9e5362eb587ea415ee401dbec3c5"
hardening = ["vis"]


@subpackage("kgraphviewer-devel")
def _(self):
    return self.default_devel()
