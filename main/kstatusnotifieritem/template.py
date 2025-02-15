pkgname = "kstatusnotifieritem"
pkgver = "6.11.0"
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
    "qt6-qtbase-private-devel",  # qwidgetwindow_p.h
    "qt6-qttools-devel",
]
pkgdesc = "KDE Implementation of Status Notifier Items"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/kstatusnotifieritem"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kstatusnotifieritem-{pkgver}.tar.xz"
sha256 = "26c92c25b1f70296bde9e71fba1f719778c85cb57227f6045f606af99c48a8bd"
hardening = ["vis"]


@subpackage("kstatusnotifieritem-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
