pkgname = "kstatusnotifieritem"
pkgver = "6.17.0"
pkgrel = 2
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
sha256 = "678a9bfc870066d5413bbcfa09a56b82b0affd2bc222ce5701d02a8b129edd91"
hardening = ["vis"]


@subpackage("kstatusnotifieritem-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
