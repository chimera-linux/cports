pkgname = "kauth"
pkgver = "6.12.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kcoreaddons-devel",
    "kwindowsystem-devel",
    "polkit-qt-1-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Execute actions as privileged user"
license = "LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/kauth"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kauth-{pkgver}.tar.xz"
sha256 = "04cf4f1c2d1ecdeb78cfd986e21d48ab531acbe69420f343207dd66da8ff9d93"
hardening = ["vis"]


@subpackage("kauth-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
