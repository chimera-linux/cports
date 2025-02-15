pkgname = "kiconthemes"
pkgver = "6.11.0"
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
pkgdesc = "KDE Icon GUI utilities"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://api.kde.org/frameworks/kiconthemes/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kiconthemes-{pkgver}.tar.xz"
sha256 = "1671ab3fd9b1e0753a7062bab80f5489f3ac750ecb30b91db99a6689988afb87"
hardening = ["vis"]


@subpackage("kiconthemes-devel")
def _(self):
    return self.default_devel()
