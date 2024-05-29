pkgname = "kauth"
pkgver = "6.2.0"
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
sha256 = "3511d9d857c0f6962b005b381ec5e2fef9ded59244da14e31dd0673e05a69b0a"
# FIXME: cfi kills systemsettings in libKF6AuthCore.so
hardening = ["vis", "!cfi"]


@subpackage("kauth-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
