pkgname = "plasma-activities"
pkgver = "6.4.4"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Core components for KDE's Activity Manager"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/plasma/plasma-activities"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-activities-{pkgver}.tar.xz"
sha256 = "ab810aa594ed3386f6a8564705ea2a46cc62ec367de2039625e030f6af955fe8"
hardening = ["vis"]


@subpackage("plasma-activities-devel")
def _(self):
    return self.default_devel()
