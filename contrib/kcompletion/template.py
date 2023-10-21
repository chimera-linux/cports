pkgname = "kcompletion"
pkgver = "6.2.0"
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
sha256 = "58cb938eb111e8859dd1baa51062467f226b8c67cb1fdb98748d3e97fabf08e9"
# FIXME: cfi crashes kio kurl*test & e.g. kwrite save file dialog upon first char of filename in libKF6Completion.so
hardening = ["vis", "!cfi"]


@subpackage("kcompletion-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
