pkgname = "kauth"
pkgver = "6.3.0"
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
sha256 = "ebcf36816ff826a2cfb3ed0a0d3746d7da9a23f79901ec43b7a4e7b156af33b5"
# FIXME: cfi kills systemsettings in libKF6AuthCore.so
hardening = ["vis", "!cfi"]


@subpackage("kauth-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
