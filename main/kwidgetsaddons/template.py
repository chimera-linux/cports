pkgname = "kwidgetsaddons"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only AND LGPL-2.1-only AND Unicode-DFS-2016"
url = "https://api.kde.org/frameworks/kwidgetsaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kwidgetsaddons-{pkgver}.tar.xz"
sha256 = "bd36342893863e6110c5f1245f8ae0b3a338275f4eaf124b15585d2fe492329a"
hardening = ["vis"]
# fails
options = ["!cross"]


@subpackage("kwidgetsaddons-devel")
def _(self):
    return self.default_devel()
