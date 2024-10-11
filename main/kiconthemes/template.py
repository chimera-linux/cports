pkgname = "kiconthemes"
pkgver = "6.7.0"
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
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Icon GUI utilities"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://api.kde.org/frameworks/kiconthemes/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kiconthemes-{pkgver}.tar.xz"
sha256 = "be25bff1f5f65edd45b24ff9beda44b04c0e22d193e72458c96a5c591b70b968"
hardening = ["vis"]


@subpackage("kiconthemes-devel")
def _(self):
    return self.default_devel()
