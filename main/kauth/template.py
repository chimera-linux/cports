pkgname = "kauth"
pkgver = "6.15.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = [
    "kcoreaddons-devel",
    "kwindowsystem-devel",
    "polkit-qt-1-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE Execute actions as privileged user"
license = "LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/kauth"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kauth-{pkgver}.tar.xz"
sha256 = "19c7b598a780ba5befd30f25de694536811a46a5622c4a2c28892f2f3ba5a617"
hardening = ["vis"]


@subpackage("kauth-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
