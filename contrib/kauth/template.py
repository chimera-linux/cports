pkgname = "kauth"
pkgver = "6.4.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/kauth"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kauth-{pkgver}.tar.xz"
)
sha256 = "0598e205dedc670af3a077ba02110a44db2f9d5e55df5003b0fc2490ac2ff1ce"
hardening = ["vis"]


@subpackage("kauth-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
