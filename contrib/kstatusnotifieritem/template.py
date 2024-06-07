pkgname = "kstatusnotifieritem"
pkgver = "6.3.0"
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
sha256 = "ce1f2e33d0dbe81a48f0040977b7b7aa7234f6a003173e395b3de5d783398cd8"
hardening = ["vis", "!cfi"]


@subpackage("kstatusnotifieritem-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
