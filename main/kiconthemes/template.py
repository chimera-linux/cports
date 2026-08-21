pkgname = "kiconthemes"
pkgver = "6.29.0"
pkgrel = 0
build_style = "cmake"
# flaky tests when parallel
make_check_args = ["-j1"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "breeze-icons-devel",
    "karchive-devel",
    "kcolorscheme-devel",
    "kconfigwidgets-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "qt6-qtbase-private-devel",  # qguiapplication_p.h/qiconloader_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
depends = ["qt6-qtsvg"]
pkgdesc = "KDE Icon GUI utilities"
license = "LGPL-2.1-only"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kiconthemes-{pkgver}.tar.xz"
sha256 = "233de4cd2fef5b7b4ce1e317196407d25300b767614a93e160b45ac34710223d"
hardening = ["vis"]


@subpackage("kiconthemes-devel")
def _(self):
    return self.default_devel()
