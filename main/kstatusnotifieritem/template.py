pkgname = "kstatusnotifieritem"
pkgver = "6.13.0"
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
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/kstatusnotifieritem"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kstatusnotifieritem-{pkgver}.tar.xz"
sha256 = "ed387fdee3dcb5bc3fa956ef6bb99bd2d4c0ed56ee5e2f1d89abaeb0c0b4de9a"
hardening = ["vis"]


@subpackage("kstatusnotifieritem-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
