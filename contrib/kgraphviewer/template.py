pkgname = "kgraphviewer"
pkgver = "2.5.0"
pkgrel = 1
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
source = f"$(KDE_SITE)/kgraphviewer/{pkgver}/kgraphviewer-{pkgver}.tar.xz"
sha256 = "872bee63fb4df6f7fb2b4eaf02ff825cba3ca953ac02509a287fe5cd0f1e2b69"
hardening = ["vis"]


@subpackage("kgraphviewer-devel")
def _devel(self):
    return self.default_devel()
