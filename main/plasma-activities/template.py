pkgname = "plasma-activities"
pkgver = "6.7.4"
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
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-activities-{pkgver}.tar.xz"
sha256 = "f990e8871586c7bafe3545609b071b14c3021105cc90f603dacf45e2e0185c2a"
hardening = ["vis"]


@subpackage("plasma-activities-devel")
def _(self):
    return self.default_devel()
