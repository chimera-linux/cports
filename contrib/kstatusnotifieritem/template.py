pkgname = "kstatusnotifieritem"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kwindowsystem-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Implementation of Status Notifier Items"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/kstatusnotifieritem"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kstatusnotifieritem-{pkgver}.tar.xz"
sha256 = "04b9fc0905b614afc8e0afcf5451018d2a126f165221b6db20e4171be2fb1fcf"
hardening = ["vis", "cfi"]


@subpackage("kstatusnotifieritem-devel")
def _devel(self):
    return self.default_devel()
