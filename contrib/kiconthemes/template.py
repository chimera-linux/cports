pkgname = "kiconthemes"
pkgver = "6.3.0"
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
sha256 = "945394afc9f8207924bf07f9a6de3bee7fcd523bce87e0004d62767ab37cc303"
hardening = ["vis", "!cfi"]


@subpackage("kiconthemes-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
