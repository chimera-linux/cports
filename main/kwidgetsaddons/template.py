pkgname = "kwidgetsaddons"
pkgver = "6.17.0"
pkgrel = 0
build_style = "cmake"
# unpackaged pyside6
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
# kcolumnresizertest broken, tooltipwidget hangs indefinitely with QT_QPA_PLATFORM=offscreen
# ktimecombobox: musl locale memes
make_check_args = [
    "-E",
    "k(widgetsaddons-kcolumnresizer|tooltipwidget|timecombobox)test",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE addons to QtWidgets"
license = "GPL-2.0-only AND LGPL-2.1-only AND Unicode-DFS-2016"
url = "https://api.kde.org/frameworks/kwidgetsaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kwidgetsaddons-{pkgver}.tar.xz"
sha256 = "dcb33387953cd0429d4297d628b4872e7a3a970cce5ea84b446677d8b7487ea1"
hardening = ["vis"]
# fails
options = ["!cross"]


@subpackage("kwidgetsaddons-devel")
def _(self):
    return self.default_devel()
