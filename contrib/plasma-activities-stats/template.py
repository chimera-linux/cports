pkgname = "plasma-activities-stats"
pkgver = "6.1.2"
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
sha256 = "3896c364f03d6b77dc7dcdadec942530f2c18ea9bb27e0ed1874c382961f8a79"
hardening = ["vis", "cfi"]


@subpackage("plasma-activities-stats-devel")
def _devel(self):
    return self.default_devel()
