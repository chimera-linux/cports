pkgname = "kstatusnotifieritem"
pkgver = "6.16.0"
pkgrel = 0
build_style = "cmake"
# unpackaged pyside6
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "kwindowsystem-devel",
    "qt6-qtbase-private-devel",  # qwidgetwindow_p.h
    "qt6-qttools-devel",
]
pkgdesc = "KDE Implementation of Status Notifier Items"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/kstatusnotifieritem"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kstatusnotifieritem-{pkgver}.tar.xz"
sha256 = "73c2590b2f6fb5f61fc3b7dc021df763bf0f3969c1eab8c5d0b85df445acad20"
hardening = ["vis"]


@subpackage("kstatusnotifieritem-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
