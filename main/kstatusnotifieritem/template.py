pkgname = "kstatusnotifieritem"
pkgver = "6.10.0"
pkgrel = 1
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
sha256 = "4fa19843a737b43674d19b9ad31466c6aa64bbe27709073c3e2c33aa03bfac22"
hardening = ["vis"]


@subpackage("kstatusnotifieritem-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
