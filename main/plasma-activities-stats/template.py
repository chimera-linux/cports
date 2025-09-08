pkgname = "plasma-activities-stats"
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
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Library to access KDE activity manager statistics data"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-activities-stats"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-activities-stats-{pkgver}.tar.xz"
sha256 = "dd43899617b0cc0e927a13bfb88146b761f7390c1fba568e2e4522f07f0f5901"
hardening = ["vis"]


@subpackage("plasma-activities-stats-devel")
def _(self):
    return self.default_devel()
