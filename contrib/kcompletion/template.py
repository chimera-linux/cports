pkgname = "kcompletion"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Powerful completion framework"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcompletion/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcompletion-{pkgver}.tar.xz"
sha256 = "3f027ac6bd285d040a5038c31b10e306bd2cb099d396e88536cd149e88ee712e"
# FIXME: cfi crashes kio kurl*test & e.g. kwrite save file dialog upon first char of filename in libKF6Completion.so
hardening = ["vis", "!cfi"]


@subpackage("kcompletion-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
