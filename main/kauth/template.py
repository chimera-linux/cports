pkgname = "kauth"
pkgver = "6.28.0"
pkgrel = 0
build_style = "cmake"
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
sha256 = "fb4d90ee46a2f6202e53cdd5af8f77069c380955e3f340881f2f36ec8312079b"
hardening = ["vis"]


@subpackage("kauth-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
