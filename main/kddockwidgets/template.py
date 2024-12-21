pkgname = "kddockwidgets"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DKDDockWidgets_QT6=ON",
    "-DKDDockWidgets_EXAMPLES=OFF",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "nlohmann-json",
    "qt6-qtbase-private-devel",  # qhighdpiscaling_p.h/qquickitem_p.h
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Dock Widget Framework for Qt"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://www.kdab.com/development-resources/qt-tools/kddockwidgets"
source = f"https://github.com/KDAB/KDDockWidgets/releases/download/v{pkgver}/kddockwidgets-{pkgver}.tar.gz"
sha256 = "02672f3ae864ed278e47602bebd8e5b1051a8d592678c829c171ce812d8469b2"


@subpackage("kddockwidgets-devel")
def _(self):
    return self.default_devel()
