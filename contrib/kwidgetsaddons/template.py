pkgname = "kwidgetsaddons"
pkgver = "6.2.2"
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
sha256 = "391bd57846ad1451c4a1adfd09cfbfa8c23b14bf2b6bf710842360b57d90049d"
# FIXME: cfi kills systemsettings/kwrite etc upon "save unsaved changes?" dialog in
# https://invent.kde.org/frameworks/kwidgetsaddons/-/blob/v6.2.2/src/kmessagedialog.cpp#L496
hardening = ["vis", "!cfi"]
# fails
options = ["!cross"]


@subpackage("kwidgetsaddons-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
