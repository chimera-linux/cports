pkgname = "kstatusnotifieritem"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
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
sha256 = "80eae2693cdb5da669b4ed6a8228bddc39816aca0fde928f231e4894827d1de0"
hardening = ["vis"]


@subpackage("kstatusnotifieritem-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
