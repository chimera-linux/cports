pkgname = "kddockwidgets"
pkgver = "2.3.0"
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
sha256 = "843baf9e1812c1ab82fd81d85b57cbc0d29bb43245efeb2539039780004b1056"


@subpackage("kddockwidgets-devel")
def _(self):
    return self.default_devel()
