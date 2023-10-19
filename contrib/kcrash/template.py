pkgname = "kcrash"
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
    "kcoreaddons-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Graceful handling of application crashes"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcrash/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcrash-{pkgver}.tar.xz"
sha256 = "00b7b4885cb2a92e832816e9cc1da8cf5cccc4c4482c13648f020988c86cf588"
# FIXME: at least "./test_crasher ES" is broken
hardening = ["vis", "!cfi"]


@subpackage("kcrash-devel")
def _devel(self):
    return self.default_devel()
