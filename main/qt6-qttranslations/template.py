pkgname = "qt6-qttranslations"
pkgver = "6.11.2"
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
sha256 = "021684c1a7937a9fabc3b056a6698ad5978794caf9ac190fd6cc11399e67c014"
# locale files belong here
options = ["!autosplit"]
