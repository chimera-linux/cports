pkgname = "kauth"
pkgver = "6.18.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
sha256 = "8c6fee69482e7a3dfcf7eacca9cb6a191ec5d1b09e0a539e1f7d5d76d08403e9"
hardening = ["vis"]


@subpackage("kauth-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
