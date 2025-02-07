pkgname = "kddockwidgets"
pkgver = "2.2.1"
pkgrel = 1
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
sha256 = "8693e06abee0c88517d8480b22647702a51a0708f3c876ed5385d9a4e356e1a5"


@subpackage("kddockwidgets-devel")
def _(self):
    return self.default_devel()
