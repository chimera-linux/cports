pkgname = "qt6-qttranslations"
pkgver = "6.12.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "qt6-qttools",
]
makedepends = ["qt6-qttools-devel"]
pkgdesc = "Qt6 translations component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qttranslations-everywhere-src-{pkgver}.tar.xz"
sha256 = "85929c0c30d6f273f23bd879bb69803ea17b010ab73cab2f8abf95357f6f6bbb"
# locale files belong here
options = ["!autosplit"]
