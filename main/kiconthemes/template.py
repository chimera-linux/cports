pkgname = "kiconthemes"
pkgver = "6.6.0"
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
sha256 = "2d00b17929d886425395e96c4c18bf5e8dfbf3f1cac2dac199a6f2ac5af35b22"
hardening = ["vis"]


@subpackage("kiconthemes-devel")
def _(self):
    return self.default_devel()
