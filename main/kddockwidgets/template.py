pkgname = "kddockwidgets"
pkgver = "2.2.4"
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
    "fmt-devel",
    "nlohmann-json",
    "qt6-qtbase-private-devel",  # qhighdpiscaling_p.h/qquickitem_p.h
    "qt6-qtdeclarative-devel",
    "spdlog-devel",
]
pkgdesc = "Dock Widget Framework for Qt"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://www.kdab.com/development-resources/qt-tools/kddockwidgets"
source = f"https://github.com/KDAB/KDDockWidgets/releases/download/v{pkgver}/kddockwidgets-{pkgver}.tar.gz"
sha256 = "a1cf55a3cf267108ee495de8df9038c67f61da5ca324059cb32543d69877524e"


@subpackage("kddockwidgets-devel")
def _(self):
    return self.default_devel()
