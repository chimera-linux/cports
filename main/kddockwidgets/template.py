pkgname = "kddockwidgets"
pkgver = "2.1.0"
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
sha256 = "cf3242b8fde8988b2661366b6a9597bcb67164074c4f31d03ec2999b475a25d7"


@subpackage("kddockwidgets-devel")
def _(self):
    return self.default_devel()
