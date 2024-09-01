pkgname = "kwidgetsaddons"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
# kcolumnresizertest broken, tooltipwidget hangs indefinitely with QT_QPA_PLATFORM=offscreen
make_check_args = ["-E", "k(widgetsaddons-kcolumnresizer|tooltipwidget)test"]
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
sha256 = "cf3abcc40a619183c7d4625dc961a0b65ae593c6c41afe0aaa450e90b5d0fe09"
hardening = ["vis"]
# fails
options = ["!cross"]


@subpackage("kwidgetsaddons-devel")
def _(self):
    return self.default_devel()
