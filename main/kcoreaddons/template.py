pkgname = "kcoreaddons"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt6 addon library with a collection of non-GUI utilities"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/kcoreaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcoreaddons-{pkgver}.tar.xz"
sha256 = "48511e9dab1f2e80b3c4822bb87c2e981186de3b8977d92082d34d003b1283c5"
hardening = ["vis"]


@subpackage("kcoreaddons-devel")
def _(self):
    return self.default_devel()
