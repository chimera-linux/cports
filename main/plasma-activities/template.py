pkgname = "plasma-activities"
pkgver = "6.7.91"
pkgrel = 0
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
source = (
    f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/plasma-activities-{pkgver}.tar.xz"
)
sha256 = "37df26774ec4d5c7dfed65c6b6c2cdd32891a9aaecd0658706b7b02778175fc4"
hardening = ["vis"]


@subpackage("plasma-activities-devel")
def _(self):
    return self.default_devel()
