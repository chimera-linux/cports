pkgname = "plasma-activities-stats"
pkgver = "6.1.1"
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
sha256 = "42846790ff461ef70cdcdb7edc10f3becf095e02f9e612fa1ac7e525104db613"
hardening = ["vis", "cfi"]


@subpackage("plasma-activities-stats-devel")
def _devel(self):
    return self.default_devel()
