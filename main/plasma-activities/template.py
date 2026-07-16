pkgname = "plasma-activities"
pkgver = "6.7.3"
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
sha256 = "3a9fbf0039464270238b84344b1064c57fb11a6aa5d7900f08a0a868063a62ea"
hardening = ["vis"]


@subpackage("plasma-activities-devel")
def _(self):
    return self.default_devel()
