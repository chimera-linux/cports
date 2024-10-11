pkgname = "kauth"
pkgver = "6.7.0"
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
sha256 = "173654eee2891acd41538d31ace8b9d7ae60863bc7faef1cacec7e21c7eb1223"
hardening = ["vis"]


@subpackage("kauth-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
