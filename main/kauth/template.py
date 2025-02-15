pkgname = "kauth"
pkgver = "6.11.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kauth-{pkgver}.tar.xz"
sha256 = "479660eabe97198c31f228a18271bc739b234943c68e95383c361a835131179b"
hardening = ["vis"]


@subpackage("kauth-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
