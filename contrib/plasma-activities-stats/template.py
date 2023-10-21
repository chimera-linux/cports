pkgname = "plasma-activities-stats"
pkgver = "6.0.5"
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
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = (
    "Library to access statistics data collected by the KDE activity manager"
)
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-activities-stats"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-activities-stats-{pkgver}.tar.xz"
sha256 = "d7aaaff97b1f0c3c941b134a33f77d95af095cbb1a64efe741d7afd15c987b5f"
hardening = ["vis", "cfi"]


@subpackage("plasma-activities-stats-devel")
def _devel(self):
    return self.default_devel()
